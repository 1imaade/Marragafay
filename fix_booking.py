import os

js_path = 'js/booking-manager.js'
with open(js_path, 'r') as f:
    js_content = f.read()

# 1. Update event listener condition
old_cond = "if (e.target && (e.target.id === 'bookingForm' || e.target.id === 'booking-form')) {"
new_cond = "if (e.target && (e.target.id === 'bookingForm' || e.target.id === 'booking-form' || e.target.id === 'booking-form-activity')) {"
js_content = js_content.replace(old_cond, new_cond)

# 2. Inject Payload Tracing and Explicit Error Handling
old_insert = """        try {
            // Insert into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData]);

            if (error) throw error;"""

new_insert = """        console.log("Supabase Payload Payload:", { name: bookingData.name, phone: bookingData.phone_number, date: bookingData.date, adults: bookingData.adults, children: bookingData.children, package_name: bookingData.package_title });

        try {
            // Insert into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData]);

            if (error) {
                console.error("Supabase Insertion Error:", error);
                alert("Booking failed. Please check the console.");
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = submitBtn.dataset.originalText || 'Book Now';
                }
                return;
            }"""

if "Supabase Payload Payload" not in js_content:
    js_content = js_content.replace(old_insert, new_insert)

with open(js_path, 'w') as f:
    f.write(js_content)

# 3. Add scripts to HTML templates
scripts_to_inject = """  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script src="../js/supabase-client.js"></script>
  <script src="../js/booking-manager.js"></script>
"""

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html') and ('packages/' in root or 'activities/' in root):
            html_files.append(os.path.join(root, file))

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()
    
    if 'supabase-js' not in html:
        # inject before <script src="../js/dynamic-pricing.js"></script> or before </body>
        if '<script src="../js/dynamic-pricing.js"></script>' in html:
            html = html.replace('<script src="../js/dynamic-pricing.js"></script>', scripts_to_inject + '  <script src="../js/dynamic-pricing.js"></script>')
        else:
            html = html.replace('</body>', scripts_to_inject + '</body>')
        
        with open(file, 'w') as f:
            f.write(html)
        print(f"Injected scripts into {file}")

