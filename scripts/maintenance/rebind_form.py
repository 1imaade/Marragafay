import os
import re

# 1. Update JS
js_path = 'js/booking-manager.js'
with open(js_path, 'r') as f:
    js_content = f.read()

# Update validation
old_val = "if (!bookingData.email || !bookingData.name) {"
new_val = "if (!bookingData.name || !bookingData.phone_number) {"
js_content = js_content.replace(old_val, new_val)

# Update redirect
old_modal = """            // Prepare booking data for modal
            const confirmedBooking = {
                id: data?.[0]?.id || Math.floor(Math.random() * 10000), // Use returned ID or generate one
                name: bookingData.name,
                email: bookingData.email,
                phone_number: bookingData.phone_number,
                date: bookingData.date,
                guests: bookingData.guests,
                package_title: bookingData.package_title,
                total_price: bookingData.total_price / 10, // Backend stores MAD, display EUR
                notes: bookingData.notes,
                status: 'confirmed'
            };

            // Show the minimal booking details modal
            if (typeof window.openBookingDetailsModal === 'function') {
                window.openBookingDetailsModal(confirmedBooking);
            } else {
                // Fallback to SweetAlert if modal not loaded
                if (window.Swal) {
                    Swal.fire({
                        title: 'Booking Confirmed',
                        html: 'We have received your request.<br>We will contact you on WhatsApp shortly.',
                        icon: 'success',
                        iconColor: '#C19B76',
                        confirmButtonText: 'Perfect',
                        buttonsStyling: false,
                        customClass: {
                            popup: 'swal2-popup',
                            title: 'swal2-title',
                            htmlContainer: 'swal2-html-container',
                            confirmButton: 'swal2-confirm',
                            icon: 'swal2-icon swal2-success'
                        }
                    });
                } else {
                    alert('Booking Confirmed! We\\'ll contact you on WhatsApp shortly.');
                }
            }"""
new_modal = "            // Forcibly trigger a JavaScript redirect to the new dedicated success page\n            window.location.href = 'success.html';"
js_content = js_content.replace(old_modal, new_modal)

with open(js_path, 'w') as f:
    f.write(js_content)

# 2. Update HTML Templates
def process_html(filepath):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Check if the file has the new form structure
    if 'rounded-3xl rounded-bl-none xl:rounded-r-full xl:rounded-l-none' not in html:
        return False
        
    # Replace div with form
    old_div = '<div class="flex flex-col xl:flex-row items-stretch bg-white border border-[#10100E]/10 rounded-3xl rounded-bl-none xl:rounded-r-full xl:rounded-l-none shadow-sm w-full 2xl:w-auto">'
    new_form = '<form id="booking-form" class="flex flex-col xl:flex-row items-stretch bg-white border border-[#10100E]/10 rounded-3xl rounded-bl-none xl:rounded-r-full xl:rounded-l-none shadow-sm w-full 2xl:w-auto">'
    html = html.replace(old_div, new_form)
    
    # Fix the closing tag for the form
    button_regex = r'(<button class="[^"]*?w-full xl:w-auto bg-\[\#523225\][^"]*?">\s*Book now\s*</button>\s*)</div>'
    def replace_end(m):
        btn = m.group(1).replace('<button class="', '<button type="submit" class="')
        return btn + '</form>'
    
    html = re.sub(button_regex, replace_end, html)
    
    # Add name attributes
    html = html.replace('<input type="date" class="w-full text-[14px]', '<input type="date" name="date" required class="w-full text-[14px]')
    html = html.replace('<input type="text" placeholder="John Doe" class="w-full', '<input type="text" name="name" required placeholder="John Doe" class="w-full')
    html = html.replace('<input type="tel" placeholder="+212 600..." class="w-full', '<input type="tel" name="phone" required placeholder="+212 600..." class="w-full')
    
    # Inject hidden inputs for guests
    old_guests = '<span class="text-[12px] font-medium text-[#10100E]/50 block mb-0 xl:mb-1">Guests</span>'
    new_guests = old_guests + '\n              <input type="hidden" name="adults" id="hidden-adults" value="2">\n              <input type="hidden" name="children" id="hidden-children" value="0">'
    if 'id="hidden-adults"' not in html:
        html = html.replace(old_guests, new_guests)
        
    # Update JS script for guests
    old_js = "document.getElementById(type + '-count').textContent = counts[type];"
    new_js = "document.getElementById(type + '-count').textContent = counts[type];\n                  document.getElementById('hidden-' + type).value = counts[type];"
    if "document.getElementById('hidden-' + type)" not in html:
        html = html.replace(old_js, new_js)

    with open(filepath, 'w') as f:
        f.write(html)
    return True

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file in html_files:
    res = process_html(file)
    if res:
        print(f"Patched {file}")

