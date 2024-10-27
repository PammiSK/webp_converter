import os
from PIL import Image

def convert_webp_to_jpg():
    # Get current directory
    current_dir = os.getcwd()

    # Find all .webp files in the current directory
    webp_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.webp')]

    if not webp_files:
        print("No .webp files found in the current directory.")
        return

    # Convert each .webp file to .jpg
    for webp_file in webp_files:
        # Open the .webp image
        with Image.open(webp_file) as img:
            # Convert to RGB (JPG format doesn't support transparency)
            img = img.convert('RGB')
            # Save as .jpg
            jpg_file = webp_file.rsplit('.', 1)[0] + '.jpg'
            img.save(jpg_file, 'JPEG')
            print(f"Converted {webp_file} to {jpg_file}")

    # Delete original .webp files
    for webp_file in webp_files:
        os.remove(webp_file)
        print(f"Deleted {webp_file}")

    print("Conversion completed.")

if __name__ == "__main__":
    convert_webp_to_jpg()
