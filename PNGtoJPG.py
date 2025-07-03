# Open a python terminal window and navigate to the root folder where the PNGs you want to covert are. 
# Run the PNGtoJPG.py script from the PNG folder. 
# This will covert the PNG to JPG and put the file in the folder with the same filename (with a .jpg extension). 
# Simple, fast and clean. 

import os
from PIL import Image

# Get the current working directory
current_folder = os.getcwd()
print(f"🔍 Scanning current folder: {current_folder}")

converted_count = 0

# Loop through all files in the folder
for filename in os.listdir(current_folder):
    if filename.lower().endswith(".png"):
        png_path = os.path.join(current_folder, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(current_folder, jpg_filename)

        try:
            with Image.open(png_path) as img:
                rgb_img = img.convert("RGB")  # Convert from RGBA to RGB
                rgb_img.save(jpg_path, "JPEG")
                converted_count += 1
                print(f"✅ Converted: {filename} -> {jpg_filename}")
        except Exception as e:
            print(f"⚠️ Error converting {filename}: {e}")

print(f"\n🎉 Done! Converted {converted_count} PNG file(s) to JPG.")