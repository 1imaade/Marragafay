import os
import re

for filename in ['activities.html', 'packs.html']:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Purge unwanted classes and inject the right ones
    def nav_cleaner(match):
        nav = match.group(0)
        nav = re.sub(r'\bbg-transparent\b', '', nav)
        nav = re.sub(r'\btext-white\b', '', nav)
        nav = re.sub(r'\btext-gray-\d+\b', '', nav)
        nav = re.sub(r'\bnavbar-dark\b', '', nav)
        nav = re.sub(r'\bbg-dark\b', '', nav)
        nav = re.sub(r'\bftco_navbar\b', '', nav)
        
        # Ensure we inject the hard override classes if they aren't there
        if 'bg-[#F6F7EA]' not in nav:
            nav = re.sub(r'class="', 'class="bg-[#F6F7EA] ', nav)
        if 'text-[#10100E]' not in nav:
            nav = re.sub(r'class="', 'class="text-[#10100E] ', nav)
        
        # Clean up double spaces
        nav = re.sub(r'\s+', ' ', nav)
        nav = nav.replace('class=" ', 'class="')
        return nav

    content = re.sub(r'<nav\b[^>]*>', nav_cleaner, content)

    # 2. JavaScript Purge
    # Remove navbar-stayhere.js or any other inline script adding scroll behavior
    content = re.sub(r'<!--[^>]*Navbar JS[^>]*-->\s*<script[^>]*navbar-stayhere\.js[^>]*></script>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<script[^>]*src="[^"]*navbar-stayhere\.js"[^>]*></script>', '', content, flags=re.IGNORECASE)
    
    # Also strip out any inline scroll logic if remaining
    content = re.sub(r'<script>\s*window\.addEventListener\([\'"]scroll[\'"],\s*function\s*\(\)\s*\{.*?navbar\.classList\..*?\};\s*</script>', '', content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
