import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<section class="luxury-faq-section py-5"' in line:
        start_idx = i
        break

if start_idx != -1:
    for i in range(start_idx, len(lines)):
        if '</section>' in lines[i]:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    with open('new_faq.html', 'r', encoding='utf-8') as f:
        replacement = f.read()
    
    new_lines = lines[:start_idx] + [replacement + '\n'] + lines[end_idx+1:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Replaced FAQ section successfully from {start_idx} to {end_idx}.")
else:
    print(f"Could not find section. start_idx={start_idx}, end_idx={end_idx}")
