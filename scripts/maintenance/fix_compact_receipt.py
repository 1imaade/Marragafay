import re

with open('success.html', 'r') as f:
    html = f.read()

# 1. Geometry Shrink
# Container:
html = html.replace('max-w-[800px]', 'max-w-md')
# Card Padding:
html = html.replace('p-8 md:p-12', 'p-6 md:p-8')
# Checkmark Wrapper:
html = html.replace('w-16 h-16', 'w-12 h-12')
# Checkmark icon:
html = html.replace('<svg class="w-8 h-8', '<svg class="w-6 h-6')
# H1 text downgrade:
html = re.sub(
    r'text-4xl md:text-5xl lg:text-6xl text-\[#10100E\] tracking-tight',
    r'text-2xl font-extrabold tracking-tight leading-none text-[#10100E]',
    html
)
# Tighten gap below H1: mb-6 -> mb-4
html = html.replace('mb-6 animate-fade-up delay-100"', 'mb-4 animate-fade-up delay-100"')
html = html.replace('mb-6 animate-fade-up delay-300"', 'mb-4 animate-fade-up delay-300"')

# Strip the big paragraph:
p_to_remove = '''      <p class="text-center text-[#1C1812] text-lg mb-10 font-medium max-w-lg mx-auto leading-relaxed">
        Your expedition details have been securely logged. Our concierge team is reviewing your request.
      </p>'''
if p_to_remove in html:
    html = html.replace(p_to_remove, '')

# 2. Horizontal Data Rows
# We need to replace all 4 rows
# Row pattern:
def replace_row(match):
    full_match = match.group(0)
    label_text = match.group(1)
    span_id = match.group(2)
    
    # Force strict single-line flex
    row_classes = "flex flex-row justify-between items-center py-3 border-b border-[#10100E]/10 last:border-0"
    
    # Label styling
    label_classes = "text-[10px] md:text-[11px] font-bold uppercase tracking-widest text-[#10100E]/50"
    
    # Value styling
    value_classes = "text-sm font-semibold text-[#10100E] text-right max-w-[60%] truncate"
    
    return f'''        <div class="{row_classes} animate-fade-up">
          <span class="{label_classes}">{label_text}</span>
          <span class="{value_classes}" id="{span_id}">Loading...</span>
        </div>'''

row_pattern = r'<div class="flex flex-col sm:flex-row sm:items-center justify-between[^>]*>\s*<span class="[^"]*">([^<]+)</span>\s*<span class="[^"]*" id="([^"]+)">Loading...</span>\s*</div>'

html = re.sub(row_pattern, replace_row, html)
html = html.replace('<div class="space-y-6">', '<div class="space-y-0 w-full mb-8">') # remove y-spacing

# 3. JS Data Sanitization
# Replace the try block inside the script
old_try = r'      try \{\s*const data = JSON\.parse\(storedBooking\);\s*const packName = data\.package_name \|\| \'Custom Expedition\';\s*const date = data\.date \|\| \'To be confirmed\';\s*const guests = data\.guests_total \|\| \'1\';\s*const name = data\.name \|\| \'Valued Guest\';\s*let displayPack = packName;\s*if\(packName\.toLowerCase\(\)\.includes\(\'luxe\'\)\) displayPack = \'The Luxury Private Experience\';\s*if\(packName\.toLowerCase\(\)\.includes\(\'basic\'\)\) displayPack = \'The Discovery Experience\';\s*if\(packName\.toLowerCase\(\)\.includes\(\'comfort\'\)\) displayPack = \'The Signature Experience\';\s*document\.getElementById\(\'display-pack\'\)\.textContent = displayPack;\s*document\.getElementById\(\'display-date\'\)\.textContent = date;\s*document\.getElementById\(\'display-guests\'\)\.textContent = guests \+ \(guests == 1 \? \' Guest\' : \' Guests\'\);\s*document\.getElementById\(\'display-name\'\)\.textContent = name;\s*\} catch \(e\) \{'

new_try = '''      try {
        const data = JSON.parse(storedBooking);

        let cleanPackage = 'Custom Expedition';
        if (data.package_name) {
          cleanPackage = data.package_name.split('-')[0].split('|')[0].trim();
        }
        
        let formattedDate = 'To be confirmed';
        if (data.date) {
            try {
                formattedDate = new Date(data.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
            } catch(e) {
                formattedDate = data.date;
            }
        }
        
        const guests = data.guests_total || '1';
        const name = data.name || 'Valued Guest';

        document.getElementById('display-pack').textContent = cleanPackage;
        document.getElementById('display-date').textContent = formattedDate;
        document.getElementById('display-guests').textContent = guests + (guests == 1 ? ' Guest' : ' Guests');
        document.getElementById('display-name').textContent = name;

      } catch (e) {'''

html = re.sub(old_try, new_try, html)

with open('success.html', 'w') as f:
    f.write(html)
print("Execution Complete")
