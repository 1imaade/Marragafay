import os
import re

def fix_html_content(filepath, content):
    filename = os.path.basename(filepath)
    original = content
    
    # 1. Skip if it is a routing redirect page
    if '<title>Marragafay | Routing...</title>' in content:
        return content

    # 2. Add main-content ID for skip link
    if 'id="main-content"' not in content:
        # Check if it is a homepage (en/index.html, fr/index.html, etc.)
        is_homepage = filename == 'index.html' and any(lang in filepath for lang in ['/en/', '/fr/', '/es/', '/ar/'])
        
        if is_homepage:
            # Wrap from after </nav> to before <footer
            # Find first </nav>
            nav_index = content.find('</nav>')
            if nav_index != -1:
                # Find first <footer
                footer_index = content.find('<footer', nav_index)
                if footer_index != -1:
                    before_nav = content[:nav_index + 6]
                    middle = content[nav_index + 6:footer_index]
                    after_footer = content[footer_index:]
                    
                    content = (
                        before_nav + 
                        '\n  <main id="main-content" tabindex="-1" style="outline: none;">' + 
                        middle + 
                        '</main>\n  ' + 
                        after_footer
                    )
        else:
            # For non-homepages, add id to existing <main class="...">
            content = re.sub(
                r'<main(\s+class=["\'][^"\']*["\'])>',
                r'<main id="main-content" tabindex="-1" style="outline: none;"\1>',
                content
            )

    # 3. Replace <h4>Contact Us</h4> in modals with <h3>Contact Us</h3>
    content = re.sub(
        r'<h4 style=["\']\'Playfair Display\', serif; font-size: 1\.3rem; color: #2c3e50; margin-bottom: 20px;["\']>(.*?)</h4>',
        r'<h3 style="\'Playfair Display\', serif; font-size: 1.3rem; color: #2c3e50; margin-bottom: 20px;">\1</h3>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 4. Replace footer brand title <h1>MARRAGAFAY.</h1> with <p>
    content = re.sub(
        r'<h1 class=["\']text-\[12vw\] sm:text-\[10vw\] md:text-\[80px\] lg:text-\[120px\] xl:text-\[150px\] leading-\[0\.8\] tracking-tighter whitespace-nowrap font-bold uppercase mb-6 text-\[#F6F7EA\] -ml-1 md:-ml-2["\']>\s*MARRAGAFAY\.\s*</h1>',
        r'<p class="text-[12vw] sm:text-[10vw] md:text-[80px] lg:text-[120px] xl:text-[150px] leading-[0.8] tracking-tighter whitespace-nowrap font-bold uppercase mb-6 text-[#F6F7EA] -ml-1 md:-ml-2">\n          MARRAGAFAY.\n        </p>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 5. Replace footer column headings <h4> with <p>
    content = re.sub(
        r'<h4 class=["\']text-xs font-bold uppercase tracking-widest text-\[#F6F7EA\] mb-6["\']>(.*?)</h4>',
        r'<p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">\1</p>',
        content,
        flags=re.IGNORECASE
    )

    # 6. Boost text contrast opacities
    # text-[#10100E]/30, /40, /50, /60 -> /90 (excluding placeholder:)
    content = re.sub(
        r'(?<!placeholder:)text-\[(?i:#10100e)\]/[3456]0',
        lambda m: m.group(0).split('/')[0] + '/90',
        content
    )
    # text-[#EAE8E3]/40, /60 -> /90
    content = re.sub(
        r'text-\[(?i:#eae8e3)\]/[46]0',
        lambda m: m.group(0).split('/')[0] + '/90',
        content
    )
    # opacity-60 -> opacity-90
    content = re.sub(r'\bopacity-60\b', 'opacity-90', content)

    return content

def main():
    root_dir = '/home/imaade/Projects/Marragafay/Marragafay-main'
    updated_count = 0
    skipped_count = 0
    total_count = 0
    
    for root, dirs, files in os.walk(root_dir):
        # Skip dependency/build directories
        if any(p in root for p in ['.git', 'node_modules', '.next', '.vercel']):
            continue
            
        for file in files:
            if 'backup' in file.lower():
                continue
            if file.endswith('.html'):
                total_count += 1
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = fix_html_content(filepath, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {os.path.relpath(filepath, root_dir)}")
                    updated_count += 1
                else:
                    skipped_count += 1
                    
    print(f"\nExecution Finished:")
    print(f"Total HTML files found: {total_count}")
    print(f"Updated HTML files: {updated_count}")
    print(f"Unchanged/Skipped HTML files: {skipped_count}")

if __name__ == '__main__':
    main()
