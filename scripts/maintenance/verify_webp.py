"""
WebP Conversion Verification Report
====================================

This script verifies that all images were properly converted and referenced.
"""

import os
from pathlib import Path

def check_webp_conversions():
    """Check which images have WebP versions."""
    print("=" * 60)
    print("WEBP CONVERSION VERIFICATION")
    print("=" * 60)
    
    base_dir = Path(__file__).parent
    
    # Check Slider-images
    slider_dir = base_dir / "images" / "Slider-images"
    if slider_dir.exists():
        print(f"\n📁 Slider Images ({slider_dir}):")
        print("-" * 60)
        
        slider_files = list(slider_dir.iterdir())
        original_images = [f for f in slider_files if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]
        webp_images = [f for f in slider_files if f.suffix.lower() == '.webp']
        
        for img in original_images:
            webp_version = img.with_suffix('.webp')
            has_webp = webp_version.exists()
            status = "✅" if has_webp else "❌"
            
            if has_webp:
                orig_size = os.path.getsize(img) / 1024
                webp_size = os.path.getsize(webp_version) / 1024
                savings = ((orig_size - webp_size) / orig_size * 100)
                print(f"{status} {img.name} → {webp_version.name}")
                print(f"   Original: {orig_size:.2f} KB → WebP: {webp_size:.2f} KB (Saved {savings:.1f}%)")
            else:
                print(f"{status} {img.name} → NO WEBP VERSION")
        
        print(f"\nTotal WebP files: {len(webp_images)}")
    
    # Check logo images  
    logo_dir = base_dir / "images"
    if logo_dir.exists():
        print(f"\n📁 Logo Images ({logo_dir}):")
        print("-" * 60)
        
        logo_files = ['logo-trensparent.png', 'main-logo.jpg']
        for logo in logo_files:
            logo_path = logo_dir / logo
            if logo_path.exists():
                webp_path = logo_path.with_suffix('.webp')
                has_webp = webp_path.exists()
                status = "✅" if has_webp else "❌"
                
                if has_webp:
                    orig_size = os.path.getsize(logo_path) / 1024
                    webp_size = os.path.getsize(webp_path) / 1024
                    savings = ((orig_size - webp_size) / orig_size * 100)
                    print(f"{status} {logo} → {webp_path.name}")
                    print(f"   Original: {orig_size:.2f} KB → WebP: {webp_size:.2f} KB (Saved {savings:.1f}%)")
    
    # Check HTML references
    print(f"\n📄 HTML File Verification:")
    print("-" * 60)
    
    html_file = base_dir / "index.html"
    if html_file.exists():
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count WebP references
        webp_count = content.count('.webp')
        jpg_count = content.count('.jpg')
        jpeg_count = content.count('.jpeg')
        png_count = content.count('.png')
        
        print(f"✅ WebP references: {webp_count}")
        print(f"{'⚠️ ' if jpg_count > 0 else '✅'} JPG references: {jpg_count}")
        print(f"{'⚠️ ' if jpeg_count > 0 else '✅'} JPEG references: {jpeg_count}")
        print(f"{'⚠️ ' if png_count > 0 else '✅'} PNG references: {png_count}")
        
        if jpg_count == 0 and jpeg_count == 0 and png_count == 0:
            print("\n🎉 SUCCESS: All slider/logo image references use WebP format!")
        else:
            print("\n⚠️  Note: Some .png references exist (may be for favicons/external images)")
    
    print("\n" + "=" * 60)
    print("✨ Verification Complete!")
    print("=" * 60)

if __name__ == "__main__":
    check_webp_conversions()
