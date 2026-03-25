/* ═══════════════════════════════════════════════════════════════════════════
   Hardware Security CWE Documentation — Client-side interactivity
   ═══════════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  const searchInput = document.getElementById('cwe-search');
  if (!searchInput) return;

  /* ── Sidebar live search/filter ─────────────────────────────────────────── */
  searchInput.addEventListener('input', function () {
    const query = this.value.trim().toLowerCase();
    const details = document.querySelectorAll('.sidebar-nav details');

    details.forEach(function (det) {
      let visibleCount = 0;
      const items = det.querySelectorAll('.cwe-list li');

      items.forEach(function (li) {
        const matches = !query || li.textContent.toLowerCase().includes(query);
        li.style.display = matches ? '' : 'none';
        if (matches) visibleCount++;
      });

      if (query) {
        /* Auto-expand categories with matches, collapse empty ones */
        det.open = visibleCount > 0;
      }
      /* Hide entire category if nothing matches */
      det.style.display = (visibleCount === 0 && query) ? 'none' : '';
    });
  });

  /* ── Keyboard shortcuts ─────────────────────────────────────────────────── */
  document.addEventListener('keydown', function (e) {
    /* Press "/" anywhere to focus the search box */
    if (e.key === '/' && document.activeElement !== searchInput &&
        document.activeElement.tagName !== 'INPUT') {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    }
    /* Escape to clear search and blur */
    if (e.key === 'Escape' && document.activeElement === searchInput) {
      searchInput.value = '';
      searchInput.dispatchEvent(new Event('input'));
      searchInput.blur();
    }
  });

})();
