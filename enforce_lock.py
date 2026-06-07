import os

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html') and ('packages' in root or 'activities' in root):
            html_files.append(os.path.join(root, file))

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()
    
    # Check if we already injected it
    if 'onsubmit="event.preventDefault();"' not in html:
        # Patch both forms
        html = html.replace('<form id="booking-form"', '<form id="booking-form" onsubmit="event.preventDefault();"')
        html = html.replace('<form id="booking-form-activity"', '<form id="booking-form-activity" onsubmit="event.preventDefault();"')
        
        with open(file, 'w') as f:
            f.write(html)
        print(f"Locked {file}")

