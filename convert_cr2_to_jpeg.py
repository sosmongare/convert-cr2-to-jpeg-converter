import rawpy  # Library for reading RAW files
import imageio  # Library for saving images
import os  # Library for interacting with the operating system

# Function to convert a single CR2 file to JPEG
def convert_cr2_to_jpeg(cr2_file_path, jpeg_file_path):
    # Read the CR2 file
    with rawpy.imread(cr2_file_path) as raw:
        # Process the raw data to get an RGB image
        rgb = raw.postprocess()
        # Save the RGB image as a JPEG file
        imageio.imsave(jpeg_file_path, rgb)

# Function to batch convert CR2 files to JPEG
def batch_convert_cr2_to_jpeg(input_folder, output_folder):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a CR2 file
        if filename.lower().endswith('.cr2'):
            # Construct the full path to the CR2 file
            cr2_file_path = os.path.join(input_folder, filename)
            # Construct the full path for the output JPEG file
            jpeg_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
            # Convert the CR2 file to JPEG
            convert_cr2_to_jpeg(cr2_file_path, jpeg_file_path)
            # Print a message indicating the conversion is complete
            print(f'Converted {filename} to JPEG.')

# Example usage:
# Define the input folder containing CR2 files
input_folder = 'E:/church backup/23 06 2024/cr2'
# Define the output folder to save JPEG files
output_folder = 'E:/church backup/23 06 2024/jpeg'
# Call the batch conversion function
batch_convert_cr2_to_jpeg(input_folder, output_folder)