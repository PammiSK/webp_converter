import os
import datetime
from PIL import Image

def get_log_file_path():
    # Get the current timestamp for the log file name
    timestamp = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
    log_file_name = f"webp_conversion_{timestamp}.txt"

    # Check if the specified directory exists
    log_dir = r"C:\Users\Siva\OneDrive\webp_converter\conversion_logs"
    if not os.path.exists(log_dir):
        # If the directory doesn't exist, use the current directory
        log_dir = os.getcwd()

    # Return the full path for the log file
    return os.path.join(log_dir, log_file_name)

def log_message(log_file, message=""):
    with open(log_file, 'a') as log:
        log.write(message + '\n')
    print(message)

def convert_webp_to_jpg():
    # Prepare log file
    log_file = get_log_file_path()
    
    # Get current directory
    current_dir = os.getcwd()
    log_message(log_file, f"Current directory: {current_dir}")

    # Find all .webp files in the current directory
    webp_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.webp')]
    
    if not webp_files:
        error_message = "No .webp files found in the current directory."
        log_message(log_file, error_message)
        return

    # Convert each .webp file to .jpg
    for webp_file in webp_files:
        try:
            # Open the .webp image
            with Image.open(webp_file) as img:
                # Convert to RGB (JPG format doesn't support transparency)
                img = img.convert('RGB')
                # Save as .jpg
                jpg_file = webp_file.rsplit('.', 1)[0] + '.jpg'
                img.save(jpg_file, 'JPEG')
                # Log the conversion
                log_message(log_file, f"Converted {webp_file} to {jpg_file}")
        except Exception as e:
            # Log any conversion errors
            log_message(log_file, f"Failed to convert {webp_file}: {e}")

    # Delete original .webp files
    for webp_file in webp_files:
        try:
            os.remove(webp_file)
            # Log the deletion
            log_message(log_file, f"Deleted {webp_file}")
        except Exception as e:
            # Log any deletion errors
            log_message(log_file, f"Failed to delete {webp_file}: {e}")

    log_message(log_file, "Conversion completed.")

if __name__ == "__main__":
    convert_webp_to_jpg()
