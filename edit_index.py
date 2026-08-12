import sys

file_path = r'E:\PANDIRAAGENCY\SAE-AQIQAH\Report-website\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement 1: CSS
target_css = """  footer p { color: var(--theme-text-muted); font-size: 0.82rem; }

  @media (max-width: 720px) {
    .grid-2, .grid-3 { grid-template-columns: 1fr; }
    .job-head { flex-direction: column; gap: calc(var(--space-unit)*2); }
    .nav-links { display: none; }"""

replacement_css = """  footer p { color: var(--theme-text-muted); font-size: 0.82rem; }

  /* ===== mobile nav toggle ===== */
  .mobile-nav-toggle {
    display: none;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: calc(var(--space-unit) * 1);
    gap: 6px;
    flex-direction: column;
    z-index: 99;
  }
  .mobile-nav-toggle .bar {
    width: 25px;
    height: 2px;
    background-color: var(--theme-text);
    border-radius: 2px;
    transition: all var(--transition-fast) ease-in-out;
  }
  /* animation when active */
  .mobile-nav-toggle.active .bar:nth-child(1) { transform: translateY(8px) rotate(45deg); }
  .mobile-nav-toggle.active .bar:nth-child(2) { opacity: 0; }
  .mobile-nav-toggle.active .bar:nth-child(3) { transform: translateY(-8px) rotate(-45deg); }

  @media (max-width: 720px) {
    .grid-2, .grid-3 { grid-template-columns: 1fr; }
    .job-head { flex-direction: column; gap: calc(var(--space-unit)*2); }
    
    .mobile-nav-toggle { display: flex; }
    
    .nav-links {
      display: flex;
      flex-direction: column;
      position: absolute;
      top: 100%;
      left: 0;
      width: 100%;
      background: color-mix(in srgb, var(--theme-bg) 95%, transparent);
      backdrop-filter: blur(10px);
      padding: calc(var(--space-unit) * 4);
      gap: calc(var(--space-unit) * 3);
      border-bottom: 1px solid var(--theme-border);
      opacity: 0;
      visibility: hidden;
      transform: translateY(-10px);
      transition: all var(--transition-fast) ease-in-out;
    }
    .nav-links.active {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }"""

if target_css in content:
    content = content.replace(target_css, replacement_css)
    print("Replaced CSS")
else:
    print("CSS target not found")

# Replacement 2: HTML Button
target_html = """    </div>
  </div>
  <div class="nav-links">"""

replacement_html = """    </div>
  </div>
  <button class="mobile-nav-toggle" aria-label="Toggle navigation">
    <span class="bar"></span>
    <span class="bar"></span>
    <span class="bar"></span>
  </button>
  <div class="nav-links">"""

if target_html in content:
    content = content.replace(target_html, replacement_html)
    print("Replaced HTML")
else:
    print("HTML target not found")

# Replacement 3: Javascript
target_js = """</script>

</body>
</html>"""

replacement_js = """</script>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (mobileNavToggle && navLinks) {
      mobileNavToggle.addEventListener('click', () => {
        mobileNavToggle.classList.toggle('active');
        navLinks.classList.toggle('active');
      });

      // Close mobile nav when clicking a link
      const links = navLinks.querySelectorAll('a');
      links.forEach(link => {
        link.addEventListener('click', () => {
          mobileNavToggle.classList.remove('active');
          navLinks.classList.remove('active');
        });
      });
    }
  });
</script>

</body>
</html>"""

if target_js in content:
    content = content.replace(target_js, replacement_js)
    print("Replaced JS")
else:
    print("JS target not found")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
