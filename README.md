## WebP to JPG Converter

This script converts all `.webp` images in the current directory to `.jpg` format, deletes the original `.webp` files, and logs the process. The log file contains details about the conversions and any errors encountered.

### Features

- Automatically finds and converts all `.webp` files in the current directory.
- Converts `.webp` images to `.jpg` format.
- Deletes the original `.webp` files after successful conversion.
- Logs the conversion and deletion of files, as well as any errors encountered.
- Saves log files with a timestamped name in a specified log directory or the current directory if the specified one doesn't exist.

### Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) library (PIL fork for image processing)

### Installation

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install the Pillow library**:
   ```
   pip install Pillow
   ```

### Usage

1. **Place the script in the directory where you have the `.webp` files**.

2. **Run the script**:
   ```
   python webp_converter.py
   ```

3. **Output**:
   - The script will look for `.webp` files in the current directory, convert them to `.jpg`, delete the original `.webp` files, and log the details.

### Logging

- The script generates a log file named `webp_conversion_YY_MM_DD_HH_mm_SS.txt` where `YY_MM_DD_HH_mm_SS` is the timestamp when the script was run.
- The log file is saved in `C:\Users\Siva\OneDrive\webp_converter\conversion_logs` if the directory exists. Otherwise, it is saved in the current directory.
- The log file contains information about:
  - The current working directory.
  - Conversion details of each file.
  - Deletion details of the original `.webp` files.
  - Any errors encountered during conversion or deletion.

### Example Log File Content

```
Current directory: C:\path\to\your\directory
Converted image1.webp to image1.jpg
Converted image2.webp to image2.jpg
Deleted image1.webp
Deleted image2.webp
Conversion completed.
```

### Error Handling

- If there are no `.webp` files in the current directory, the script will log a message stating that no `.webp` files were found.
- If any errors occur during conversion or deletion, the error message will be logged.

### Customization

- **Log Directory**: You can change the default log directory by modifying the `log_dir` variable in the `get_log_file_path()` function.

### Limitations

- The script only processes `.webp` files in the current working directory.
- It does not support recursive search in subdirectories.

### License

This script is open-source and licensed under the MIT License. See the `LICENSE` file for more information. 

### Troubleshooting

- **No .webp files found**: Make sure there are `.webp` files in the directory where the script is run.
- **Permission errors**: Ensure you have the necessary file permissions for the directory.

### Converting to Executable

You can convert this script to an executable using `pyinstaller`:
```
pyinstaller --onefile --noconsole webp_converter.py
```
This will create a standalone `.exe` file for easier use on Windows systems.