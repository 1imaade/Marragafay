import os
import re

# List of HTML files to update (excluding backups, node_modules, and font files)
html_files = [
    'index.html',
    'activities.html',
    'about.html',
    'blog.html',
    'blog-single.html',
    'checkout.html',
    'contact.html',
    'reviews.html',
    'packs.html',
    'activities/quad-biking.html',
    'activities/paragliding.html',
    'activities/hot-air-balloon.html',
    'activities/dinner-show.html',
    'activities/camel-ride.html',
    'activities/buggy.html',
    'packages/luxe.html',
    'packages/comfort.html',
    'packages/basic.html'
]

# Favicon tags template
def get_favicon_tags(path_prefix=''):
    """Generate favicon tags with appropriate path prefix for subdirectories"""
    return f'''  <link rel="icon" type="image/png" href="{path_prefix}images/logo/logo-high-res.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{path_prefix}images/logo/logo-high-res.png">
  <link rel="shortcut icon" type="image/png" href="{path_prefix}images/logo/logo-high-res.png">'''

def add_favicon_to_file(filepath):
    """Add or update favicon tags in an HTML file"""
    
    # Determine if file is in subdirectory (needs ../ prefix)
    path_prefix = '../' if '/' in filepath or '\\' in filepath else ''
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if favicon already exists
        if 'logo-high-res.png' in content:
            print(f"✓ {filepath} - Already has favicon (skipped)")
            return False
        
        # Look for existing favicon tags to replace
        favicon_patterns = [
            r'\s*<link rel="icon"[^>]*>',
            r'\s*<link rel="apple-touch-icon"[^>]*>',
            r'\s*<link rel="shortcut icon"[^>]*>',
            r'\s*<link rel="icon" type="image/png" sizes="\d+x\d+" href="[^"]+">',
        ]
        
        # Remove old favicon tags
        for pattern in favicon_patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE | re.MULTILINE)
        
        # Find the best place to insert favicon (before </head> or after last <link> tag)
        favicon_tags = get_favicon_tags(path_prefix)
        
        # Try to insert after the last stylesheet link before </head>
        head_match = re.search(r'(.*<link[^>]*stylesheet[^>]*>)\s*', content, re.DOTALL)
        if head_match:
            # Find the position after the last <link> tag
            last_link_pos = content.rfind('<link', 0, content.find('</head>'))
            if last_link_pos != -1:
                # Find the end of that link tag
                link_end_pos = content.find('>', last_link_pos) + 1
                # Insert favicon after it
                content = content[:link_end_pos] + '\n' + favicon_tags + '\n' + content[link_end_pos:]
            else:
                # Fallback: insert before </head>
                content = content.replace('</head>', f'{favicon_tags}\n</head>')
        else:
            # Fallback: insert before </head>
            content = content.replace('</head>', f'{favicon_tags}\n</head>')
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(content)
        
        print(f"✓ {filepath} - Favicon added successfully")
        return True
        
    except Exception as e:
        print(f"✗ {filepath} - Error: {str(e)}")
        return False

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Adding Favicon to All HTML Pages")
    print("=" * 60)
    print()
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for html_file in html_files:
        if os.path.exists(html_file):
            result = add_favicon_to_file(html_file)
            if result:
                updated_count += 1
            elif result is False and 'Already has favicon' in str(result):
                skipped_count += 1
        else:
            print(f"✗ {html_file} - File not found")
            error_count += 1
    
    print()
    print("=" * 60)
    print(f"Summary: {updated_count} updated, {skipped_count} skipped, {error_count} errors")
    print("=" * 60)
