"""
Image to WebP Converter
Converts all JPG, JPEG, and PNG images to WebP format with quality=80
to reduce file sizes while maintaining good visual quality.
"""

import os
from pathlib import Path
from PIL import Image

def convert_to_webp(image_path, quality=80):
    """
    Convert an image to WebP format.
    
    Args:
        image_path: Path to the original image
        quality: WebP quality (0-100, default 80)
    
    Returns:
        tuple: (original_size, new_size) in bytes, or (0, 0) if conversion failed
    """
    try:
        # Get original file size
        original_size = os.path.getsize(image_path)
        
        # Open and convert image
        img = Image.open(image_path)
        
        # Convert RGBA to RGB if necessary (WebP supports RGBA, but we'll ensure compatibility)
        if img.mode in ('RGBA', 'LA', 'P'):
            # For images with transparency, keep RGBA
            pass
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Create output path (same directory, .webp extension)
        webp_path = os.path.splitext(image_path)[0] + '.webp'
        
        # Skip if WebP already exists
        if os.path.exists(webp_path):
            print(f"⏭️  Skipped (already exists): {webp_path}")
            return (0, 0)
        
        # Save as WebP
        img.save(webp_path, 'WEBP', quality=quality, method=6)
        
        # Get new file size
        new_size = os.path.getsize(webp_path)
        
        # Calculate savings
        savings = original_size - new_size
        savings_percent = (savings / original_size * 100) if original_size > 0 else 0
        
        print(f"✅ Converted: {os.path.basename(image_path)}")
        print(f"   Original: {original_size / 1024:.2f} KB → WebP: {new_size / 1024:.2f} KB")
        print(f"   Saved: {savings / 1024:.2f} KB ({savings_percent:.1f}%)")
        
        return (original_size, new_size)
        
    except Exception as e:
        print(f"❌ Error converting {image_path}: {str(e)}")
        return (0, 0)

def process_directory(directory, quality=80):
    """
    Process all images in a directory recursively.
    
    Args:
        directory: Path to the directory to process
        quality: WebP quality (0-100)
    
    Returns:
        tuple: (total_original_size, total_new_size, count)
    """
    total_original = 0
    total_new = 0
    count = 0
    
    # Supported extensions
    extensions = {'.jpg', '.jpeg', '.png'}
    
    print(f"\n📁 Processing directory: {directory}")
    print("-" * 60)
    
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if file has supported extension
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in extensions:
                file_path = os.path.join(root, file)
                original_size, new_size = convert_to_webp(file_path, quality)
                
                if original_size > 0 and new_size > 0:
                    total_original += original_size
                    total_new += new_size
                    count += 1
    
    return (total_original, total_new, count)

def main():
    """Main function to process images in specified directories."""
    print("=" * 60)
    print("🖼️  IMAGE TO WEBP CONVERTER")
    print("=" * 60)
    
    # Get script directory (project root)
    script_dir = Path(__file__).parent
    
    # Directories to process
    directories = [
        script_dir / 'images',
        script_dir / 'Slider-images'
    ]
    
    # WebP quality setting
    quality = 80
    
    # Track totals across all directories
    grand_total_original = 0
    grand_total_new = 0
    grand_total_count = 0
    
    # Process each directory
    for directory in directories:
        if directory.exists():
            total_original, total_new, count = process_directory(directory, quality)
            grand_total_original += total_original
            grand_total_new += total_new
            grand_total_count += count
        else:
            print(f"\n⚠️  Directory not found: {directory}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 CONVERSION SUMMARY")
    print("=" * 60)
    print(f"Total images converted: {grand_total_count}")
    print(f"Original total size: {grand_total_original / 1024 / 1024:.2f} MB")
    print(f"New total size: {grand_total_new / 1024 / 1024:.2f} MB")
    
    if grand_total_original > 0:
        total_savings = grand_total_original - grand_total_new
        total_savings_percent = (total_savings / grand_total_original * 100)
        print(f"Total space saved: {total_savings / 1024 / 1024:.2f} MB ({total_savings_percent:.1f}%)")
    else:
        print("No images were converted.")
    
    print("=" * 60)
    print("\n✨ Done!")

if __name__ == "__main__":
    main()
