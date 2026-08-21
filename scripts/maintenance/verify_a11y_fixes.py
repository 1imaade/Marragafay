import os
import re

def verify_html(filepath, content):
    filename = os.path.basename(filepath)
    rel_path = os.path.relpath(filepath, '/home/imaade/Projects/Marragafay/Marragafay-main')
    
    # Skip routing redirect pages
    if '<title>Marragafay | Routing...</title>' in content:
        return True, ""
        
    errors = []

    # 1. id="main-content" check
    if 'id="main-content"' not in content:
        errors.append("Missing id=\"main-content\" for skip link target")
        
    # 2. Check modal header hierarchy
    if re.search(r'<h4 style=["\']\'Playfair Display\', serif; font-size: 1\.3rem; color: #2c3e50; margin-bottom: 20px;["\']>', content):
        errors.append("Contains unsequential <h4> header inside modals")
        
    # 3. Check footer brand title (should not be in h1)
    if re.search(r'<h1 class=["\']text-\[12vw\].*?["\']>\s*MARRAGAFAY\.\s*</h1>', content, re.DOTALL):
        errors.append("Contains <h1> brand title inside footer (breaks hierarchy)")

    # 4. Check footer column headings (should not be in h4)
    if re.search(r'<h4 class=["\']text-xs font-bold uppercase tracking-widest text-\[#F6F7EA\] mb-6["\']>', content):
        errors.append("Contains <h4> column headings inside footer (breaks hierarchy)")

    # 5. Check opacities (any remaining text-[#10100E]/[3456]0 or text-[#EAE8E3]/[46]0, except placeholders)
    low_contrast_matches = re.findall(r'(?<!placeholder:)text-\[(?i:#10100e)\]/[3-6]0', content)
    if low_contrast_matches:
        errors.append(f"Contains low-contrast text opacity classes: {low_contrast_matches}")
        
    low_contrast_eae_matches = re.findall(r'text-\[(?i:#eae8e3)\]/[46]0', content)
    if low_contrast_eae_matches:
        errors.append(f"Contains low-contrast text opacity classes: {low_contrast_eae_matches}")

    if errors:
        return False, f"{rel_path}: " + " | ".join(errors)
    return True, ""

def verify_css():
    css_path = '/home/imaade/Projects/Marragafay/Marragafay-main/css/navbar-stayhere.css'
    if not os.path.exists(css_path):
        return False, "css/navbar-stayhere.css does not exist"
        
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
        
    errors = []
    
    # Check .skip-to-content focus rule
    if 'position: fixed;' not in css_content or 'top: 10px;' not in css_content:
        errors.append("Missing fixed positioning or coordinates for .skip-to-content:focus")
        
    # Check min-height for mobile menu toggle and language selectors
    if 'min-height: 44px' not in css_content:
        errors.append("Missing min-height: 44px for mobile touch targets")
        
    if errors:
        return False, "CSS Errors: " + " | ".join(errors)
    return True, ""

def main():
    root_dir = '/home/imaade/Projects/Marragafay/Marragafay-main'
    passed_count = 0
    failed_count = 0
    total_count = 0
    
    # Verify CSS first
    css_ok, css_err = verify_css()
    if not css_ok:
        print(f"CSS Validation Failed:\n{css_err}\n")
    else:
        print("CSS Validation Passed: Skip links and mobile touch target styles conform.\n")
        
    # Verify HTML files
    for root, dirs, files in os.walk(root_dir):
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
                    
                ok, err = verify_html(filepath, content)
                if not ok:
                    print(err)
                    failed_count += 1
                else:
                    passed_count += 1
                    
    print(f"\nVerification Finished:")
    print(f"CSS conforms: {css_ok}")
    print(f"Total HTML files audited: {total_count}")
    print(f"Passed HTML files: {passed_count}")
    print(f"Failed HTML files: {failed_count}")
    
    if failed_count > 0 or not css_ok:
        print("\nVerification STATUS: FAILED")
        exit(1)
    else:
        print("\nVerification STATUS: PASSED")
        exit(0)

if __name__ == '__main__':
    main()
