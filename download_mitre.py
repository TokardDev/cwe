#!/usr/bin/env python3
"""
Script to download CWE (Common Weakness Enumeration) data from MITRE.
Downloads HTML pages for specified CWE IDs and saves them to data/websites/
"""

import os
import sys
import time
import argparse
import requests
from pathlib import Path
from typing import List, Optional

# Base URL for CWE definitions
CWE_BASE_URL = "https://cwe.mitre.org/data/definitions/{cwe_id}.html"

# Output directory
OUTPUT_DIR = Path(__file__).parent / "data" / "websites"


def download_cwe(cwe_id: int, output_dir: Path, delay: float = 1.0) -> Optional[Path]:
    """
    Download a single CWE page from MITRE.

    Args:
        cwe_id: The CWE identifier number (e.g., 1342)
        output_dir: Directory to save the downloaded file
        delay: Delay in seconds between requests (be nice to MITRE servers)

    Returns:
        Path to saved file, or None if download failed
    """
    url = CWE_BASE_URL.format(cwe_id=cwe_id)
    output_file = output_dir / f"cwe-{cwe_id}.html"

    # Skip if already downloaded
    if output_file.exists():
        print(f"[SKIP] CWE-{cwe_id} already exists")
        return output_file

    try:
        print(f"[DOWNLOADING] CWE-{cwe_id} from {url}")

        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; CWE-Downloader/1.0; Security Research)"
        }

        response = requests.get(url, headers=headers, timeout=30)

        # Check for 404 - CWE doesn't exist
        if response.status_code == 404:
            print(f"[NOT FOUND] CWE-{cwe_id} does not exist")
            return None

        response.raise_for_status()

        # Save the HTML content
        output_file.write_text(response.text, encoding="utf-8")
        print(f"[SAVED] {output_file}")

        # Be nice to the server
        time.sleep(delay)

        return output_file

    except requests.RequestException as e:
        print(f"[ERROR] Failed to download CWE-{cwe_id}: {e}")
        return None


def download_multiple(cwe_ids: List[int], output_dir: Path, delay: float = 1.0) -> dict:
    """
    Download multiple CWE pages.

    Returns:
        Dict with 'success', 'failed', and 'skipped' counts
    """
    results = {"success": 0, "failed": 0, "skipped": 0}

    for cwe_id in cwe_ids:
        result = download_cwe(cwe_id, output_dir, delay)
        if result:
            if "SKIP" in str(result):
                results["skipped"] += 1
            else:
                results["success"] += 1
        else:
            results["failed"] += 1

    return results


def download_range(start: int, end: int, output_dir: Path, delay: float = 1.0) -> dict:
    """Download a range of CWE IDs."""
    cwe_ids = list(range(start, end + 1))
    return download_multiple(cwe_ids, output_dir, delay)


def parse_cwe_ids(ids_str: str) -> List[int]:
    """
    Parse CWE IDs from string. Supports:
    - Single ID: "1342"
    - Multiple IDs: "1342,1343,1344"
    - Ranges: "1342-1350"
    - Mixed: "1342,1345-1350,1400"
    """
    ids = []
    parts = ids_str.split(",")

    for part in parts:
        part = part.strip()
        if "-" in part:
            # Range (e.g., "1342-1350")
            start, end = part.split("-", 1)
            ids.extend(range(int(start.strip()), int(end.strip()) + 1))
        else:
            # Single ID
            ids.append(int(part))

    return sorted(set(ids))  # Remove duplicates and sort


def main():
    parser = argparse.ArgumentParser(
        description="Download CWE data from MITRE",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s 1342                    # Download single CWE
  %(prog)s 1342,1343,1344          # Download multiple CWEs
  %(prog)s 1342-1350               # Download range of CWEs
  %(prog)s 1342,1400-1420,1500     # Mixed format
  %(prog)s --list-existing         # Show already downloaded CWEs
        """
    )

    parser.add_argument(
        "cwe_ids",
        nargs="?",
        help="CWE ID(s) to download. Supports: single (1342), list (1342,1343), range (1342-1350)"
    )

    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=1.0,
        help="Delay between requests in seconds (default: 1.0)"
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=OUTPUT_DIR,
        help=f"Output directory (default: {OUTPUT_DIR})"
    )

    parser.add_argument(
        "--list-existing",
        action="store_true",
        help="List already downloaded CWE files"
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download even if file exists"
    )

    args = parser.parse_args()

    # Ensure output directory exists
    args.output.mkdir(parents=True, exist_ok=True)

    # List existing files
    if args.list_existing:
        existing = sorted(args.output.glob("cwe-*.html"))
        if existing:
            print(f"Found {len(existing)} downloaded CWE files:")
            for f in existing:
                print(f"  {f.name}")
        else:
            print("No CWE files downloaded yet.")
        return 0

    # Must provide CWE IDs if not listing
    if not args.cwe_ids:
        parser.print_help()
        return 1

    # Parse and download
    try:
        cwe_ids = parse_cwe_ids(args.cwe_ids)
    except ValueError as e:
        print(f"Error parsing CWE IDs: {e}")
        return 1

    print(f"Will download {len(cwe_ids)} CWE(s) to {args.output}")
    print("-" * 50)

    # If force, remove existing files first
    if args.force:
        for cwe_id in cwe_ids:
            existing = args.output / f"cwe-{cwe_id}.html"
            if existing.exists():
                existing.unlink()

    results = download_multiple(cwe_ids, args.output, args.delay)

    print("-" * 50)
    print(f"Done! Success: {results['success']}, Failed: {results['failed']}, Skipped: {results['skipped']}")

    return 0 if results["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
