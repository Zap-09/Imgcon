import argparse

from convert_function import *


parser = argparse.ArgumentParser(description="Image format converter command line.")

parser.add_argument("-i", "--input_file", help="Enter the filename/path, use '/' for finding all the images in the directory",required=True)
parser.add_argument("-o", "--output_folder", help="Enter output path, keep empty for current directory")
parser.add_argument("-e", "--extension", help="Select the output extension type",required=True)

arg = parser.parse_args()

input_file = arg.input_file

output_folder = arg.output_folder

ext = arg.extension

if __name__ == "__main__":
    if input_file == "/":
        input_file = None

    main(ext=ext,image_folder=input_file,output_folder=output_folder)

