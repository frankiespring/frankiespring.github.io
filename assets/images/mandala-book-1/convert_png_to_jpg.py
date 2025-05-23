import os
from PIL import Image

def process_and_rename_images(folder_path, base_name="sample"):
    """
    Processes image files in a folder:
    - Converts .png to .jpg (if not already .jpg).
    - Renames all processed images sequentially as sample1.jpg, sample2.jpg, etc.
    - Replaces original files in the same folder.

    Args:
        folder_path (str): The path to the folder containing the images.
        base_name (str): The base name for the new JPG files (e.g., "sample").
    """
    image_files = []
    # Collect all image files (PNG, JPG, JPEG)
    for f in os.listdir(folder_path):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(f)

    # Sort files alphabetically to ensure consistent numbering
    # (e.g., 'a.png' will be processed before 'b.jpg')
    image_files.sort()

    processed_count = 0
    for filename in image_files:
        original_filepath = os.path.join(folder_path, filename)
        new_filename_base = f"{base_name}{processed_count + 1}"
        new_filepath_jpg = os.path.join(folder_path, f"{new_filename_base}.jpg")

        try:
            with Image.open(original_filepath) as img:
                # Handle PNGs with transparency by converting to RGB with a white background
                if img.mode == 'RGBA':
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[3]) # Use alpha channel as mask
                    img = background
                elif img.mode != 'RGB':
                    # Convert other modes (e.g., L for grayscale) to RGB
                    img = img.convert('RGB')

                # Save as JPG. If original was already JPG and RGB, it's effectively resaved.
                img.save(new_filepath_jpg, "JPEG", quality=85) # Quality 85 is a good balance

            # Delete the original file only if the new file was successfully created
            # And only if the original file path is different from the new one
            # (which it almost always will be due to renaming)
            if original_filepath != new_filepath_jpg:
                os.remove(original_filepath)
            print(f"Processed: '{filename}' -> '{new_filepath_jpg}'")
            processed_count += 1

        except Exception as e:
            print(f"Error processing '{filename}': {e}")

# --- How to use it in VS Code ---
if __name__ == "__main__":
    # IMPORTANT: Set this to the path of your 'folder1'
    # If you place this Python script directly inside 'folder1' and run it from there,
    # then '.' (dot) refers to the current directory.
    target_folder = "." # Change this to the actual path if the script is elsewhere
                        # e.g., "C:/Users/YourName/Pictures/folder1" or "/home/yourname/images/folder1"

    print(f"Starting image processing in: {os.path.abspath(target_folder)}")
    process_and_rename_images(target_folder)
    print("\n--- Processing Complete ---")
    print(f"All image files in '{os.path.abspath(target_folder)}' should now be JPGs named sequentially.")

