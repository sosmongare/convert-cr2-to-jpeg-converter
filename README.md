# Convert CR2 to JPEG

`convert_cr2_to_jpeg.py` is a Python script designed to convert Canon RAW image files (CR2) to JPEG format. This script is ideal for photographers and users who need to process CR2 files into a more widely supported format for easier viewing and sharing.

## Features
- Converts CR2 files to JPEG format.
- Preserves image quality during conversion.
- Supports batch processing of multiple CR2 files.
- User-friendly and simple to use.

## Requirements

Before using the script, ensure you have the following installed:

- Python 3.6 or higher
- Required Python packages:
  - `imageio`
  - `rawpy`

You can install the required packages using pip:

```bash
pip install imageio rawpy
```

## Usage

1. Place the `convert_cr2_to_jpeg.py` script in the same directory as your CR2 files, or provide a path to the folder containing the CR2 files.
2. Run the script from the command line:

```bash
python convert_cr2_to_jpeg.py <input_folder> <output_folder>
```

### Arguments
- `<input_folder>`: The folder containing the CR2 files to be converted.
- `<output_folder>`: The folder where the converted JPEG files will be saved.

### Example

```bash
python convert_cr2_to_jpeg.py ./raw_images ./jpeg_images
```

## Notes
- Ensure that the input folder contains valid CR2 files.
- The output folder will be created if it does not exist.
- Converted images will have the same base filename as the original CR2 files, but with a `.jpeg` extension.

## Troubleshooting
- **Error: No module named 'rawpy' or 'imageio':** Install the missing package using pip.
- **CR2 file not converting:** Verify that the file is a valid CR2 file and not corrupted.
- **Permission Denied:** Ensure you have write access to the specified output folder.

## License

This script is provided "as is" under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request on the [repository](#).

## Acknowledgements

This script uses the following libraries:
- [imageio](https://imageio.github.io/)
- [rawpy](https://pypi.org/project/rawpy/)
