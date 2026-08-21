#!/usr/bin/env python3
"""
Marragafay Full Project HTML Cleanup Script
Processes all HTML files across all language directories.
"""

import glob
import re

def fix_html_structure(content):
    """
    If there is content after </html>, move it inside </body>
    """
    body_match = re.search(r'</body>', content)
    html_match = re.search(r'</html>', content)
    if not body_match or not html_match:
        return content

    html_end_pos = html_match.end()
    orphaned = content[html_end_pos:].strip()
    if not orphaned:
        return content

    before_body_close = content[:body_match.start()]
    new_content = before_body_close + '\n' + orphaned + '\n\n</body>\n\n</html>\n'
    return new_content

def remove_unused_fonts(content):
    """
    Remove the Google Fonts preload link for unused fonts
    (EB Garamond, Playfair Display, Eczar, Open Sans, Overpass, Montserrat).
    """
    p1 = re.compile(
        r'<link rel="preload" as="style"\s*\n?\s*href="https://fonts\.googleapis\.com/css2\?family=EB\+Garamond[^"]*"\s*\n?\s*onload="[^"]*">\s*\n?',
        re.MULTILINE
    )
    content = p1.sub('', content)

    p2 = re.compile(
        r'<noscript>\s*\n?\s*<link rel="stylesheet"\s*\n?\s*href="https://fonts\.googleapis\.com/css2\?family=EB\+Garamond[^"]*">\s*\n?\s*</noscript>\s*\n?',
        re.MULTILINE
    )
    content = p2.sub('', content)
    return content

def remove_dead_font_css(content):
    """
    Remove unused font CSS class definitions from inline styles.
    """
    patterns = [
        re.compile(r'[ \t]*/\* Open Sans font class for future use \*/\s*\n[ \t]*\.open-sans-uniquifier \{[^}]+\}\s*\n', re.MULTILINE),
        re.compile(r'[ \t]*/\* Eczar font class for future use \*/\s*\n[ \t]*\.eczar-uniquifier \{[^}]+\}\s*\n', re.MULTILINE),
        re.compile(r'[ \t]*/\* Global font application - Removed old Overpass styles \*/\s*\n', re.MULTILINE),
    ]
    for p in patterns:
        content = p.sub('', content)
    return content

def remove_console_logs(content):
    """
    Remove console.log() statements from inline <script> blocks.
    """
    pattern = re.compile(r'^[ \t]*console\.log\(.*?\);\s*\n', re.MULTILINE)
    content = pattern.sub('', content)
    return content

def get_all_target_files():
    all_files = glob.glob('**/*.html', recursive=True)
    targets = []
    for f in all_files:
        # Exclude node_modules, .next, .git, and root router index/page files
        if f.startswith(('node_modules/', '.next/', '.git/')):
            continue
        # Don't touch the root language router files (index.html, about.html at root, etc.)
        if '/' not in f:
            continue
        targets.append(f)
    return sorted(targets)

if __name__ == '__main__':
    target_files = get_all_target_files()
    print(f"Found {len(target_files)} target HTML files to process.")
    
    total_saved_bytes = 0
    fixed_structure_count = 0
    cleaned_font_count = 0
    cleaned_log_count = 0

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        orig_size = len(original)
        
        # Check before states
        had_orphaned = False
        html_idx = original.rfind('</html>')
        if html_idx != -1 and len(original[html_idx + 7:].strip()) > 0:
            had_orphaned = True
        
        had_fonts = 'family=EB+Garamond' in original
        had_logs = 'console.log(' in original
        
        content = fix_html_structure(original)
        content = remove_unused_fonts(content)
        content = remove_dead_font_css(content)
        content = remove_console_logs(content)
        
        new_size = len(content)
        saved = orig_size - new_size
        total_saved_bytes += saved
        
        if had_orphaned:
            fixed_structure_count += 1
        if had_fonts:
            cleaned_font_count += 1
        if had_logs:
            cleaned_log_count += 1
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        status = []
        if had_orphaned: status.append("HTML Fixed")
        if had_fonts: status.append("Fonts Cleaned")
        if had_logs: status.append("Logs Removed")
        status_str = ", ".join(status) if status else "Clean (no change needed)"
        
        print(f"✓ {filepath:<35} | {status_str}")

    print("\n" + "="*50)
    print(f"🎉 Cleanup Summary:")
    print(f"  • Total files processed: {len(target_files)}")
    print(f"  • HTML structures fixed: {fixed_structure_count} files")
    print(f"  • Unused fonts removed:  {cleaned_font_count} files")
    print(f"  • Console logs cleaned:  {cleaned_log_count} files")
    print(f"  • Total file size saved: {total_saved_bytes / 1024:.1f} KB")
    print("="*50)
