import os
import re

def fix_html(content):
    original = content
    
    # 1. Fix text contrast for text-[#F6F7EA]/40, /50, /60 -> /90
    # Case-insensitive match for the color hex, but keep the case intact in replacement, or just replace with original match.
    content = re.sub(
        r'text-\[(?i:#f6f7ea)\]/[456]0',
        lambda m: m.group(0)[:-2] + '90',
        content
    )
    
    # Also check if there are other opacity like 70 or 30 just in case? The prompt said "like text-[#f6f7ea]/50".
    # I'll replace /30 and /70 as well if they exist, but /40 /50 /60 are the main contrast issues.
    
    # 2. Add aria-label to the fixed whatsapp floating button
    # The button starts with <a href="https://wa.me/..." target="_blank" class="fixed bottom-6 right-6 ...
    # We will insert aria-label before the class
    content = re.sub(
        r'(<a\s+href="https://wa\.me/[^"]*"\s*(?:id="[^"]*"\s*)?(?:target="_blank"\s*)?)class="fixed\s+bottom-6',
        r'\1aria-label="Contact Marragafay Concierge on WhatsApp" class="fixed bottom-6',
        content,
        flags=re.IGNORECASE
    )
    
    # Wait, the class might have line breaks, or the target might be on a different line.
    # Let's use a more robust regex that finds the href and the specific class
    # Actually, in the grep output, it looks like:
    # <a href="https://wa.me/212672531624?text=..."
    #    target="_blank"
    #    class="fixed bottom-6 right-6 ...">
    # So we can use re.DOTALL or just match the class.
    
    # Let's do a more robust approach: Find all <a ...> tags. If it has wa.me and class="fixed bottom-6", inject aria-label.
    def inject_aria(match):
        tag = match.group(0)
        if 'wa.me' in tag and 'fixed' in tag and 'bottom-6' in tag and 'aria-label' not in tag:
            return tag.replace('class="', 'aria-label="Contact Marragafay Concierge on WhatsApp" class="', 1)
        return tag

    content = re.sub(r'<a\s+[^>]*>', inject_aria, content, flags=re.IGNORECASE)

    return content

count = 0
for root, dirs, files in os.walk('/home/imaade/Projects/Marragafay/Marragafay-main'):
    if '.git' in root or 'node_modules' in root or '.next' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = fix_html(content)
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Updated {count} HTML files")
