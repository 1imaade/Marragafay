"""
Update HTML Image References to WebP
Replaces .jpg, .jpeg, and .png references with .webp in src attributes,
but ONLY if the .webp file actually exists.
"""

import os
import re
from pathlib import Path

def find_all_webp_files(base_dir):
    """
    Find all .webp files in the project.
    
    Returns:
        set: Set of relative paths (from base_dir) to all .webp files
    """
    webp_files = set()
    base_path = Path(base_dir)
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith('.webp'):
                full_path = Path(root) / file
                # Get relative path from base directory
                rel_path = full_path.relative_to(base_path)
                webp_files.add(str(rel_path).replace('\\', '/'))
    
    return webp_files

def update_html_images(html_path, base_dir):
    """
    Update image references in HTML file to use .webp versions.
    
    Args:
        html_path: Path to the HTML file
        base_dir: Base directory of the project
    
    Returns:
        int: Number of replacements made
    """
    print(f"\n📄 Processing: {html_path}")
    print("-" * 60)
    
    # Read HTML content
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all .webp files in the project
    print("🔍 Scanning for existing .webp files...")
    webp_files = find_all_webp_files(base_dir)
    print(f"   Found {len(webp_files)} .webp files")
    
    # Pattern to match src="..." attributes with image extensions
    # This matches: src="path/to/image.jpg" or src="path/to/image.png" etc.
    pattern = r'src=["\']([^"\']*?\.(?:jpg|jpeg|png))(["\'])'
    
    replacements = 0
    original_content = content
    
    def replace_if_exists(match):
        nonlocal replacements
        original_src = match.group(1)
        quote = match.group(2)
        
        # Convert to .webp path
        webp_src = re.sub(r'\.(jpg|jpeg|png)$', '.webp', original_src, flags=re.IGNORECASE)
        
        # Normalize path for comparison (remove leading /, convert backslashes)
        normalized_src = webp_src.lstrip('/').replace('\\', '/')
        
        # Check if .webp file exists
        webp_file_path = Path(base_dir) / normalized_src
        
        # Also check in webp_files set (relative paths)
        if webp_file_path.exists() or normalized_src in webp_files:
            print(f"✅ {original_src} → {webp_src}")
            replacements += 1
            return f'src="{webp_src}{quote}'
        else:
            # Keep original if .webp doesn't exist
            print(f"⏭️  Skipped (no .webp): {original_src}")
            return match.group(0)
    
    # Replace all matches
    content = re.sub(pattern, replace_if_exists, content, flags=re.IGNORECASE)
    
    # Write back if changes were made
    if replacements > 0:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✨ Made {replacements} replacements in {os.path.basename(html_path)}")
    else:
        print(f"\n⚠️  No replacements made in {os.path.basename(html_path)}")
    
    return replacements

def main():
    """Main function to update HTML files."""
    print("=" * 60)
    print("🔄 HTML IMAGE REFERENCES UPDATER")
    print("=" * 60)
    
    # Get script directory (project root)
    script_dir = Path(__file__).parent
    
    # HTML file to update
    html_file = script_dir / 'index.html'
    
    if not html_file.exists():
        print(f"❌ Error: {html_file} not found!")
        return
    
    # Update HTML file
    total_replacements = update_html_images(html_file, script_dir)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 UPDATE SUMMARY")
    print("=" * 60)
    print(f"Total image references updated: {total_replacements}")
    print("=" * 60)
    print("\n✨ Done!")

if __name__ == "__main__":
    main()
