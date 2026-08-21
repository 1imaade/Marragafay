import os

scripts_to_inject = """  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script src="../js/supabase-client.js"></script>
  <script src="../js/booking-manager.js"></script>
"""

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
    
    if 'supabase-js@2' not in html:
        html = html.replace('</body>', scripts_to_inject + '</body>')
        with open(file, 'w') as f:
            f.write(html)
        print(f"Injected scripts into {file}")

