import os
from PIL import Image
from pathlib import Path

def optimize_images():
    # Define paths
    static_dir = os.path.join('portfolio', 'static')
    img_dir = os.path.join(static_dir, 'img')
    
    # Create optimized directory if it doesn't exist
    optimized_dir = os.path.join(static_dir, 'img', 'optimized')
    os.makedirs(optimized_dir, exist_ok=True)
    
    # Supported image formats
    img_formats = ('.jpg', '.jpeg', '.png')
    
    # Process each image
    for root, _, files in os.walk(img_dir):
        for file in files:
            if file.lower().endswith(img_formats) and 'optimized' not in root:
                try:
                    img_path = os.path.join(root, file)
                    rel_path = os.path.relpath(img_path, img_dir)
                    output_path = os.path.join(optimized_dir, os.path.splitext(rel_path)[0] + '.webp')
                    
                    # Create output directory structure
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    # Open and optimize image
                    with Image.open(img_path) as img:
                        # Convert to RGB if RGBA
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        
                        # Resize if too large
                        max_size = (1920, 1080)
                        img.thumbnail(max_size, Image.LANCZOS)
                        
                        # Save as WebP with 80% quality
                        img.save(
                            output_path,
                            'WEBP',
                            quality=80,
                            optimize=True,
                            progressive=True
                        )
                    
                    print(f"Optimized: {file} -> {output_path}")
                    
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")

if __name__ == "__main__":
    print("Starting image optimization...")
    optimize_images()
    print("Image optimization completed!")
