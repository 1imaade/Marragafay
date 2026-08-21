import os
import re

preload_tag = '<link rel="preload" fetchpriority="high" as="image" href="/images/Slider-images/slider-4.webp" type="image/webp">\n'

count = 0
for root, dirs, files in os.walk('/home/imaade/Projects/Marragafay/Marragafay-main'):
    if '.git' in root or 'node_modules' in root or '.next' in root:
        continue
    for file in files:
        if file == 'index.html':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if preload_tag.strip() not in content:
                # Add preload tag inside <head> (e.g. before closing </head>)
                content = content.replace('</head>', f'  {preload_tag}</head>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Added preload tag to {count} index.html files")
