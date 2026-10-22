# ZipCompressor

A simple Python script to compress files and folder contents individually into ZIP archives.

## Project Description

This project scans a given directory and:
- compresses each file into its own ZIP archive
- compresses the contents of each subfolder into a separate ZIP archive
- saves all generated ZIP files in an output folder

It is useful for organizing and packaging files without losing the original folder structure inside each archive.

## Features

- Compresses individual files into separate `.zip` files
- Compresses all contents inside each folder into one ZIP
- Uses Python's built-in `zipfile` module
- Easy to configure by setting input and output directories

## Requirements

- Python 3.x

## How to Use

1. Update the input directory path:
   ```python
   input_directory_path = r"/path/to/your/input/folder"
   ```

2. Update the output directory path:
   ```python
   output_directory_path = r"/path/to/your/output/folder"
   ```

3. Run the script:
   ```bash
   python ZipCompressor.py
   ```

## Example

If your input folder contains:

```text
input/
├── file1.txt
├── file2.txt
├── folderA/
│   ├── a.txt
│   └── b.txt
└── folderB/
    └── c.csv
```

The script will create ZIP files like:

```text
output/
├── file1.txt.zip
├── file2.txt.zip
├── folderA_contents.zip
└── folderB_contents.zip
```

## Code

```python
import os
from zipfile import ZipFile


def zip_individual_files_and_folder(directory, output_folder):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            output_path = os.path.join(output_folder, f"{item}.zip")
            with ZipFile(output_path, "w") as zipf:
                zipf.write(item_path, os.path.basename(item_path))
            print(f"{item} تم ضغطه بنجاح")

        elif os.path.isdir(item_path):
            base_name = os.path.basename(item_path)
            output_path = os.path.join(output_folder, f"{base_name}_contents.zip")
            with ZipFile(output_path, "w") as zipf:
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, item_path)
                        zipf.write(file_path, arcname)
            print(f"{base_name} تم ضغط محتوياته بنجاح")


if __name__ == "__main__":
    input_directory_path = r"/path/to/your/input/folder"
    output_directory_path = r"/path/to/your/output/folder"
    zip_individual_files_and_folder(input_directory_path, output_directory_path)
```

## Notes

- The script does not delete the original files by default.
- You can uncomment the delete line if you want to remove source files after zipping:
  ```python
  # os.remove(item_path)
  ```

## License

This project is provided as-is for educational and personal use.

## Author

Saleh MK
