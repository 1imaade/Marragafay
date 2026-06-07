import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update the booking wrapper if needed
    old_wrapper = 'class="flex flex-col xl:flex-row items-stretch bg-white border border-[#10100E]/10 rounded-none shadow-sm w-full 2xl:w-auto"'
    new_wrapper = 'class="flex flex-col xl:flex-row items-stretch bg-white border border-[#10100E]/10 rounded-xl xl:rounded-full shadow-sm w-full 2xl:w-auto"'
    content = content.replace(old_wrapper, new_wrapper)

    # 2. Update vertical padding of inputs from `py-3` to `py-2 xl:py-3` and margin of labels
    content = content.replace('px-4 py-3 w-full', 'px-4 py-2 xl:py-3 w-full')
    content = content.replace('block mb-1', 'block mb-0 xl:mb-1')

    # 3. Update the Book Now button
    old_btn = 'class="w-full xl:w-auto bg-[#523225] text-white px-8 py-3 text-[15px] font-medium hover:bg-[#3d251b] transition-colors whitespace-nowrap rounded-r-2xl border border-[#10100E]/10 border-l-0"'
    new_btn = 'class="w-full xl:w-auto bg-[#523225] text-white px-8 py-3 text-[15px] font-medium hover:bg-[#3d251b] transition-colors whitespace-nowrap rounded-b-xl rounded-t-none xl:rounded-b-none xl:rounded-r-2xl border border-[#10100E]/10 xl:border-l-0"'
    content = content.replace(old_btn, new_btn)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
