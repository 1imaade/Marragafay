#!/usr/bin/env python3
import re

FILES = ['en/index.html','fr/index.html','es/index.html','ar/index.html']

def fix_html_structure(content):
    body_match = re.search(r'</body>', content)
    html_match = re.search(r'</html>', content)
    if not body_match or not html_match:
        print("  WARNING: Could not find tags")
        return content
    html_end_pos = html_match.end()
    orphaned = content[html_end_pos:].strip()
    if not orphaned:
        print("  No orphaned content")
        return content
    before_body_close = content[:body_match.start()]
    new_content = before_body_close + '\n' + orphaned + '\n\n</body>\n\n</html>\n'
    print(f"  Fixed: moved {len(orphaned.splitlines())} orphaned lines inside </body>")
    return new_content

def remove_unused_fonts(content):
    before = len(content)
    p1 = re.compile(r'<link rel="preload" as="style"\s*\n\s*href="https://fonts\.googleapis\.com/css2\?family=EB\+Garamond[^"]*"\s*\n\s*onload="[^"]*">', re.MULTILINE)
    content = p1.sub('', content)
    p2 = re.compile(r'<noscript>\s*\n?\s*<link rel="stylesheet"\s*\n?\s*href="https://fonts\.googleapis\.com/css2\?family=EB\+Garamond[^"]*">\s*\n?\s*</noscript>', re.MULTILINE)
    content = p2.sub('', content)
    print(f"  Removed unused Google Fonts ({before - len(content)} chars)")
    return content

def remove_dead_font_css(content):
    patterns = [
        re.compile(r'[ \t]*/\* Open Sans font class for future use \*/\s*\n[ \t]*\.open-sans-uniquifier \{[^}]+\}\s*\n', re.MULTILINE),
        re.compile(r'[ \t]*/\* Eczar font class for future use \*/\s*\n[ \t]*\.eczar-uniquifier \{[^}]+\}\s*\n', re.MULTILINE),
        re.compile(r'[ \t]*/\* Global font application - Removed old Overpass styles \*/\s*\n', re.MULTILINE),
    ]
    for p in patterns:
        content = p.sub('', content)
    print("  Cleaned dead font CSS classes")
    return content

def remove_console_logs(content):
    pattern = re.compile(r'^[ \t]*console\.log\(.*?\);\s*\n', re.MULTILINE)
    count = len(pattern.findall(content))
    content = pattern.sub('', content)
    print(f"  Removed {count} console.log() statements")
    return content

for filepath in FILES:
    print(f"\nProcessing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original_size = len(content)
    content = fix_html_structure(content)
    content = remove_unused_fonts(content)
    content = remove_dead_font_css(content)
    content = remove_console_logs(content)
    new_size = len(content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Done: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB (saved {(original_size-new_size)/1024:.1f}KB)")

print("\nAll files processed!")
