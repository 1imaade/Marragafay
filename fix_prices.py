import re
import os

replacements = {
    'packages/comfort.html': '49',
    'packages/luxe.html': '89',
    'activities/quad-biking.html': '25',
    'activities/camel-ride.html': '10',
    'activities/buggy.html': '80',
    'activities/hot-air-balloon.html': '100',
    'activities/paragliding.html': '65',
    'activities/dinner-show.html': '15'
}

# The regex matches the specific span containing the price.
# For example: <span class="text-[32px] font-bold text-[#523225] tracking-tight">35 €</span>
pattern = r'(<span class="text-\[32px\] font-bold text-\[\#523225\] tracking-tight">)\d+\s*€(</span>)'

for filepath, new_price in replacements.items():
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Replace the price
        new_content = re.sub(pattern, rf'\g<1>{new_price} €\g<2>', content)
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath} to {new_price} €")
    else:
        print(f"File {filepath} not found.")

