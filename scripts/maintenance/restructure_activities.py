import re
import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading index.html: {e}")
        return

    # Find </nav> or </header>
    nav_end = content.find('</nav>')
    if nav_end != -1:
        nav_end += len('</nav>')
    else:
        nav_end = content.find('</header>')
        if nav_end != -1:
            nav_end += len('</header>')
        else:
            print("Could not find </nav> or </header>")
            return

    # Find <footer
    footer_start = content.find('<footer')
    if footer_start == -1:
        print("Could not find <footer")
        return

    top = content[:nav_end]
    bottom = content[footer_start:]

    # Remove classes from nav tag
    def modify_nav(match):
        nav_tag = match.group(0)
        # Remove target classes
        nav_tag = nav_tag.replace('bg-transparent', '')
        nav_tag = nav_tag.replace('text-[#F6F7EA]', '')
        nav_tag = nav_tag.replace('text-white', '')
        # Inject new classes
        # Find class attribute
        class_match = re.search(r'class="([^"]*)"', nav_tag)
        if class_match:
            old_classes = class_match.group(1)
            new_classes = old_classes + " bg-[#F6F7EA] text-[#10100E]"
            nav_tag = nav_tag[:class_match.start(1)] + new_classes + nav_tag[class_match.end(1):]
        else:
            # If no class attribute, add it before >
            nav_tag = nav_tag[:-1] + ' class="bg-[#F6F7EA] text-[#10100E]">'
        return nav_tag

    top = re.sub(r'<nav[^>]*>', modify_nav, top, count=1)

    # Delete JavaScript related to navbar scroll-transparency
    # We look for <script> blocks that might contain it in bottom or top.
    # We will remove inline scripts containing 'scroll' and 'navbar' or 'ftco_navbar'
    def script_cleaner(match):
        script_content = match.group(0).lower()
        if 'scroll' in script_content and ('nav' in script_content or 'header' in script_content):
            return ''
        return match.group(0)

    script_pattern = re.compile(r'<script\b[^>]*>[\s\S]*?</script>', re.IGNORECASE)
    bottom = script_pattern.sub(script_cleaner, bottom)
    top = script_pattern.sub(script_cleaner, top)

    skeleton = """
    <main class="bg-[#F6F7EA] min-h-screen pt-40 pb-24 flex flex-col">
      <div class="max-w-7xl mx-auto px-6 md:px-16 w-full">
        <h1 class="text-[12vw] sm:text-[10vw] md:text-[80px] lg:text-[120px] leading-[0.8] tracking-tighter text-[#10100E] uppercase mb-8">ACTIVITIES.</h1>
        <p class="text-[#10100E]/60 max-w-2xl text-lg mb-16">Curated high-adrenaline and authentic cultural escapes in the Agafay stone desert.</p>
        </div>
    </main>
"""

    new_content = top + skeleton + bottom

    with open('activities.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("activities.html overwritten successfully.")

if __name__ == '__main__':
    main()
