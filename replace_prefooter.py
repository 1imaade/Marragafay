import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Replace the slogan section
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<section class="pro-slogan-section" id="marragafay-slogan-box">' in line:
        start_idx = i
        break

if start_idx != -1:
    for i in range(start_idx, len(lines)):
        if '</section>' in lines[i]:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    with open('new_prefooter.html', 'r', encoding='utf-8') as f:
        replacement = f.read()
    
    new_lines = lines[:start_idx] + [replacement + '\n'] + lines[end_idx+1:]
    lines = new_lines
    print(f"Replaced prefooter section successfully from {start_idx} to {end_idx}.")
else:
    print(f"Could not find prefooter section. start_idx={start_idx}, end_idx={end_idx}")

# 2. Remove Typed.js script tag
lines = [line for line in lines if '<script src="https://unpkg.com/typed.js' not in line]

# 3. Remove the Typed JS init block
# It starts at: var sloganElement = document.getElementById('typed-slogan-v2');
# Wait, let's just find the script tag containing `new Typed('#typed-slogan-v2'`
script_start = -1
script_end = -1
for i, line in enumerate(lines):
    if "var sloganElement = document.getElementById('typed-slogan-v2');" in line:
        # found the block, let's go up to the closest <script> tag if they are wrapped, or just delete the block
        # the block is inside an inline <script> tag. Let's find the closing tag.
        script_start = i
        break

if script_start != -1:
    # let's find where the block ends.
    # It ends when we see console.log('Typed.js V2 initialized successfully'); and the closing } of the if block
    for i in range(script_start, len(lines)):
        if "console.log('Typed.js V2 initialized successfully');" in lines[i]:
            # The next lines are `    }` and `  </script>`
            script_end = i + 2 # approximately
            break
            
    if script_end != -1:
        # let's just delete from script_start to script_end
        # wait, let's just make sure we don't delete too much
        # actually, looking at the code:
        """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
        ...
        var sloganElement = ...
        if(sloganElement) {
           ...
           console.log(...);
        }
        ...
        """
        # If it's inside DOMContentLoaded, just removing the typed.js code is safer.
        # Let's just comment it out or remove those exact lines.
        del lines[script_start:script_end+1]
        print("Removed typed.js initialization block.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
