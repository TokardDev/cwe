# AI Agent Instructions - CWE Scenario Generation

This document provides instructions for an AI agent to generate CWE (Common Weakness Enumeration) scenario files based on MITRE data.

## Overview

Your task is to:
1. Download the CWE HTML page from MITRE
2. Analyze the content to extract relevant information
3. Determine if one or multiple attack scenarios are needed
4. Create a `cwe-<id>.md` file following the established structure

---

## Step 1: Download the CWE Data

Use the provided download script to fetch the CWE HTML page:

```bash
python download_mitre.py <CWE_ID>
```

Example:
```bash
python download_mitre.py 79
```

The HTML file will be saved to `data/websites/cwe-<id>.html`.

If the file already exists, use `--force` to re-download:
```bash
python download_mitre.py --force <CWE_ID>
```

---

## Step 2: Analyze the HTML Content

Read the downloaded HTML file and extract the following information from the MITRE page:

### Required Data Points

1. **CWE Title**: The official name of the weakness
2. **Description**: The detailed explanation of the weakness
3. **Extended Description**: Additional context and technical details
4. **Common Consequences**: Impact on Confidentiality, Integrity, and Availability
5. **Demonstrative Examples**: Code examples or attack scenarios provided by MITRE
6. **Observed Examples**: Real-world CVEs and incidents related to this CWE
7. **Potential Mitigations**: How the weakness can be prevented (useful for understanding attack vectors)

### Determining Number of Scenarios

**IMPORTANT**: The decision to create one or multiple scenarios must be **deeply rooted in the actual MITRE page content**. Do NOT invent multiple scenarios based on theoretical possibilities - only create multiple scenarios when the MITRE page explicitly provides distinct examples or categories.

Analyze the CWE content to decide if **one or multiple scenarios** are needed:

**Use a SINGLE scenario when:**
- The MITRE page describes a single exploitation pattern
- The Demonstrative Examples (if present) illustrate the same fundamental attack type
- The Extended Description focuses on one core mechanism
- Even if multiple CVEs are listed, they all exploit the same underlying weakness in the same way

**Use MULTIPLE scenarios ONLY when the MITRE page explicitly shows:**
- **Distinct Demonstrative Examples**: The MITRE page provides multiple code examples or attack descriptions that represent fundamentally different exploitation patterns (not just variations of the same attack)
- **Explicit Categories/Types**: The MITRE page explicitly categorizes different types of attacks (e.g., "Type 1: ...", "Type 2: ...")
- **Different Attack Contexts in Extended Description**: The Extended Description explicitly describes separate, distinct attack approaches with different mechanisms

**Key Principle**: If you need to imagine or extrapolate scenarios that aren't directly supported by content on the MITRE page, use a SINGLE scenario instead. The number of scenarios should match the distinct examples/categories provided by MITRE, not theoretical possibilities.

---

## Step 3: Determine the Correct Category Folder

Before creating the file, you must determine which category folder the CWE belongs to.

### Category Folder Mapping

CWEs are organized into Hardware Design categories based on MITRE's CWE-1194 view. Check the CWE's "MemberOf" relationship in the HTML page to find its category:

| Category ID | Folder Name | Description |
|-------------|-------------|-------------|
| 1195 | `1195-manufacturing-lifecycle/` | Manufacturing and Life Cycle Management Concerns |
| 1196 | `1196-security-flow/` | Security Flow Issues |
| 1197 | `1197-integration/` | Integration Issues |
| 1198 | `1198-privilege-access-control/` | Privilege Separation and Access Control Issues |
| 1199 | `1199-circuit-logic-design/` | General Circuit and Logic Design Concerns |
| 1201 | `1201-core-compute/` | Core and Compute Issues |
| 1202 | `1202-memory-storage/` | Memory and Storage Issues |
| 1203 | `1203-peripherals-fabric-io/` | Peripherals, On-chip Fabric, and Interface/IO Problems |
| 1205 | `1205-security-primitives-crypto/` | Security Primitives and Cryptography Issues |
| 1206 | `1206-power-clock-thermal-reset/` | Power, Clock, Thermal, and Reset Concerns |
| 1207 | `1207-debug-test/` | Debug and Test Problems |
| 1208 | `1208-cross-cutting/` | Cross-Cutting Problems |
| 1388 | `1388-physical-access/` | Physical Access Issues and Concerns |

### Finding the Category

In the downloaded HTML file, look for the "Relevant to the view 'Hardware Design'" section. Find the "MemberOf" relationship which indicates the category number (e.g., 1201, 1202).

If a CWE belongs to multiple categories, place the actual file in the **first/primary** category listed, then create symlinks in the other categories.

### Handling CWEs in Multiple Categories

When a CWE appears in multiple categories (check all "MemberOf" relationships in the HTML):

1. **Create the main file** in the primary category folder
2. **Create symlinks** in all other category folders pointing to the main file

**Creating a symlink:**
```bash
# From the project root directory
ln -s ../primary-folder/cwe-<id>.md secondary-folder/cwe-<id>.md
```

**Example:** CWE-1342 belongs to both 1201 (Core and Compute) and 1202 (Memory and Storage):
```bash
# Main file is in 1201-core-compute/cwe-1342.md
# Create symlink in 1202:
ln -s ../1201-core-compute/cwe-1342.md 1202-memory-storage/cwe-1342.md
```

---

## Step 4: File Structure

Create the file as `cwe-<id>.md` in the appropriate category folder.

### Template Structure

```markdown
# CWE-<ID> - <Official Title>

## CWE Explanation

[Your explanation of the CWE based on the MITRE content. This should be a clear, technical summary that helps readers understand the weakness, its context, and why it matters. Write this in your own words based on your analysis of the MITRE data.]

## Impact Assessment

| Aspect | Impact |
|--------|--------|
| **Confidentiality** | <impact description> |
| **Integrity** | <impact description> |
| **Availability** | <impact description> |

## Attack Scenario[s]

[Scenario content here]

---

## MITRE Reference Data

### Description

[Copy the Description directly from the MITRE page - NO EDITS]

### Extended Description

[Copy the Extended Description directly from the MITRE page - NO EDITS. If not available, write "Not available for this CWE."]

### Demonstrative Examples

[Copy the Demonstrative Examples directly from the MITRE page - NO EDITS. Include all examples with their code blocks and explanations. If not available, write "Not available for this CWE."]
```

---

## Step 4: Writing the Content

### Title Section

- Format: `# CWE-<ID> - <Title>`
- Use the exact official title from MITRE
- Example: `# CWE-79 - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')`

### CWE Explanation Section

Write a clear, technical explanation of the CWE in your own words. This section should:

1. **Explain what the weakness is**: Describe the fundamental issue in accessible but technical language
2. **Provide context**: Explain where this weakness typically occurs (hardware, software, specific components)
3. **Describe why it matters**: What makes this weakness significant from a security perspective
4. **Summarize the root cause**: What design or implementation flaw leads to this weakness

Guidelines:
- Write 2-4 paragraphs
- Use technical terminology appropriate for security professionals
- Base your explanation on the MITRE Description, Extended Description, and other content
- Do NOT copy text directly - synthesize and explain in your own words
- Focus on helping readers understand the "why" behind the weakness

Example:
```markdown
## CWE Explanation

This weakness occurs when a processor or hardware component fails to properly clear sensitive data from shared microarchitectural structures during context switches or privilege transitions. Modern processors use various internal buffers and caches to optimize performance, but these structures can retain data from previous operations.

When the hardware does not adequately flush these structures, an attacker running in a lower-privileged context may be able to observe residual data from higher-privileged operations. This is particularly dangerous in multi-tenant environments or systems where security boundaries rely on hardware isolation.

The root cause is typically a design trade-off between performance and security, where clearing all microarchitectural state would introduce unacceptable latency. However, this creates a side-channel that bypasses traditional access control mechanisms.
```

### Impact Assessment Table

Write impact descriptions following these guidelines:

| Impact Level | Description Style |
|--------------|-------------------|
| **High/Primary** | Active voice, specific outcome: "The attacker can read memory", "The attacker can extract confidential data" |
| **Low/Secondary** | "Low impact" with optional clarification in parentheses or italics: "Low impact (*System instability is possible due to inconsistent states*)" |
| **Conditional** | Describe the condition: "The attacker already has write permission on the memory" |

Examples from existing files:
- `The attacker can extract confidential data and read memory`
- `The attacker can execute commands and modify memory`
- `Low impact (An availability loss may be a result of integrity loss, but not a direct consequence of the CWE)`
- `Loss of integrity is possible`
- `Complete loss of availability is possible`

### Attack Scenarios

#### Header

- **Single scenario**: Use `## Attack Scenario` (singular)
- **Multiple scenarios**: Use `## Attack Scenarios` (plural)

#### Single Scenario Format

Write the scenario as a single paragraph directly under the header:

```markdown
## Attack Scenario

An attacker is able to [initial capability/access]. In the next step, [attack action]. [Technical details of exploitation]. [Outcome/consequence].
```

#### Multiple Scenarios Format

Use numbered subsections:

```markdown
## Attack Scenarios

### Scenario 1
[Scenario description]

### Scenario 2
[Scenario description]

### Scenario 3
[Scenario description]
```

### Writing Style for Scenarios

Follow these patterns observed in existing files:

1. **Start with attacker capability**: "An attacker is able to..."
   - `An attacker is able to corrupt a low trust application from a low trust interface`
   - `An attacker is able to execute a program with write access on limited-write non-volatile memory`
   - `An attacker is able to interact with a shadow copy of a file`
   - `An attacker runs on a hardware thread that shares physical resources with a victim thread`

2. **Describe the attack progression**: "In the next step..." or "After this..."
   - Use transitional phrases to show attack flow
   - Be specific about technical mechanisms

3. **Include technical details**:
   - Name specific techniques: "Page Fault", "General Protection Fault", "Branch Prediction manipulation"
   - Reference hardware components: "fill buffers", "store buffer", "cache", "microarchitectural structures"
   - Mention specific instruction types when relevant

4. **Explain the exploitation mechanism**:
   - Describe WHY the attack works (the weakness being exploited)
   - Include relevant conditions: "Due to the absence or incorrect implementation of..."
   - Reference timing: "during this transient window", "before the permission check officially fails"

5. **End with the consequence**:
   - "The attacker extracts this data using a side-channel analysis"
   - "This results in permanent physical damage to the memory"
   - "The attacker successfully exploits the old values, winning the race against the synchronization mechanism"

### Technical Depth Guidelines

- **Be specific**: Name actual mechanisms, not generic descriptions
- **Be technical**: Assume the reader understands security concepts
- **Be complete**: Each scenario should be self-contained and explain the full attack chain
- **Be concise**: One paragraph per scenario (typically 3-6 sentences)
- **Avoid fluff**: No introductory or concluding pleasantries

---

## Step 5: Add MITRE Reference Data

At the end of the file, add a section with the original MITRE content. This provides traceability and allows readers to reference the authoritative source.

### Description

Copy the **Description** field directly from the MITRE CWE page. Do NOT edit, rephrase, or summarize - copy it exactly as it appears.

### Extended Description

Copy the **Extended Description** field directly from the MITRE CWE page. Do NOT edit, rephrase, or summarize - copy it exactly as it appears.

If the CWE does not have an Extended Description, write: "Not available for this CWE."

### Demonstrative Examples

Copy ALL **Demonstrative Examples** from the MITRE CWE page. This includes:
- The example descriptions/explanations
- Any code blocks (preserve the original language tags and formatting)
- All examples, even if there are multiple

Do NOT edit, rephrase, or summarize - copy them exactly as they appear on the MITRE page.

If the CWE does not have Demonstrative Examples, write: "Not available for this CWE."

**Important**: The MITRE Reference Data section must be separated from the Attack Scenarios by a horizontal rule (`---`) to clearly distinguish your analysis from the original MITRE content.

---

## Step 6: Update the Index

After creating a new CWE file, update `index.md`:

### How to Update

The `index.md` file contains all CWEs as placeholders organized by category. When you create a new CWE file:

1. **Find the CWE entry** in the appropriate category section
2. **Convert the plain text entry to a link** and change the status

**Before (placeholder):**
```markdown
| CWE-1239 | Improper Zeroization of Hardware Register | Pending |
```

**After (linked):**
```markdown
| [CWE-1239](1202-memory-storage/cwe-1239.md) | Improper Zeroization of Hardware Register | Done |
```

### Updating Symlinked Entries

For CWEs that appear in multiple categories, update ALL entries in `index.md`:

**Primary category (actual file):**
```markdown
| [CWE-1342](1201-core-compute/cwe-1342.md) | Information Exposure... | Done |
```

**Secondary categories (symlinks) - add `(↗primary-category-id)` to indicate it's a symlink:**
```markdown
| [CWE-1342](1202-memory-storage/cwe-1342.md) | Information Exposure... | Done (↗1201) |
```

The `↗1201` indicates this is a symlink pointing to the main file in category 1201.

### Important Notes

- The path must match the category folder where you placed the file/symlink
- Format: `[CWE-ID](category-folder/cwe-id.md)`
- Change status from `Pending` to `Done`
- For symlinks, append `(↗primary-category-id)` to the status

---

## Quality Checklist

Before finalizing, verify:

- [ ] CWE ID and title match MITRE exactly
- [ ] CWE Explanation is present and written in your own words (not copied from MITRE)
- [ ] Impact Assessment covers all three aspects (Confidentiality, Integrity, Availability)
- [ ] Scenario header is singular/plural based on content
- [ ] Each scenario starts with attacker capability
- [ ] Technical mechanisms are named specifically
- [ ] Attack flow is clear and logical
- [ ] Consequences are explicitly stated
- [ ] MITRE Reference Data section is present with horizontal rule separator
- [ ] Description is copied exactly from MITRE (no edits)
- [ ] Extended Description is copied exactly from MITRE (or marked as not available)
- [ ] Demonstrative Examples are copied exactly from MITRE (or marked as not available)
- [ ] No trailing whitespace or formatting issues
- [ ] File ends with a blank line
- [ ] If CWE belongs to multiple categories: symlinks created in secondary folders
- [ ] All index.md entries updated (including symlinked categories with ↗ indicator)

---

## Examples Reference

Study these existing files for reference:

| File | Characteristics |
|------|-----------------|
| `1201-core-compute/cwe-1342.md` | Single scenario, transient execution |
| `1202-memory-storage/cwe-1246.md` | Single scenario, hardware/availability focus |
| `1201-core-compute/cwe-1421.md` | Three scenarios, varied attack contexts |
| `1202-memory-storage/cwe-1251.md` | Three scenarios, race condition variations |
| `1201-core-compute/cwe-1281.md` | Two scenarios, processor instruction issues |
