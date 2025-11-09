import argparse
import sys

from imgcore.convert_func import *


parser = argparse.ArgumentParser(description="Image format converter command line.")

parser.add_argument("-i", "--input_file",
                    help="Enter the filename/path of the image",
                    required=False)

parser.add_argument("-d","--directory",
                    help="Enter the folder path to convert all image files in that folder",
                    default=None,
                    required=False)

parser.add_argument("-o", "--output_folder",
                    help="Enter output path, keep empty for current directory",
                    default=None,
                    required=False)

parser.add_argument("-e", "--extension",
                    help="Select the output extension type",
                    required=False)

parser.add_argument("-q","--quality",
                    help="Sets the quality value for jpeg and webp convertion (range 1 to 100)",
                    default=None,
                    required=False,
                    type=int)

parser.add_argument("-com","--compress_level",
                    help="Sets the compress level for png(range 1 to 9 and default is 6) and webp(1 to 6 and default is 4)",
                    default=None,
                    required=False,
                    type=int)

parser.add_argument("-l","--lossless",
                    help="Lossless value for webp images default is False",
                    default=None,
                    required=False)

parser.add_argument("-opt","--optimize",
                    help="Optimize value for png images default is False",
                    default=None,
                    required=False)


args = parser.parse_args()

input_file = args.input_file

output_folder = args.output_folder

extension = args.extension

quality = args.quality

compress_level = args.compress_level

directory = args.directory

lossless = str(args.lossless).lower() == "true" if args.lossless is not None else False

optimize = str(args.optimize).lower() == "true" if args.optimize is not None else False

if not input_file and not directory:
    log("Either input_file or directory is needed for this script to run. Use -help for more info",t="Error")
    sys.exit(1)

if not extension:
    log("No extension was given. Please use png, jpeg, jpg, webp",t="error")
    sys.exit(1)

if directory:
    convert_folder(folder_path=directory,
                   ext=extension,
                   output_path=output_folder,
                   compress_level=compress_level,
                   optimize=optimize,
                   quality= quality,
                   lossless=lossless)
else:
    match extension:
        case "png":
            if quality:
                log("png does not support quality value. Ignoring this",t="warn")
                quality = None
            if lossless:
                log("png does not support lossless value. Ignoring this",t="warn")
                lossless = None

            convert_to_png(image_file=input_file,
                           output_path=output_folder,
                           compress_level=compress_level,
                           optimize=optimize)
        case "jpeg" | "jpg":
            if lossless:
                log("jpeg does not support lossless value. Ignoring this",t="warn")
                lossless = None

            if optimize:
                log("jpeg does not support optimize value. Ignoring this",t="warn")
                optimize = None

            if compress_level:
                log("jpeg does not support compress_level value. Ignoring this",t="warn")
                compress_level = None

            convert_to_jpeg(image_file=input_file,
                            output_path=output_folder,
                            quality=quality)
        case "webp":
            if optimize:
                log("webp does not support optimize value. Ignoring this", t="warn")
                optimize = None

            convert_to_webp(image_file=input_file,
                            quality=quality,
                            output_path=output_folder,
                            compress_level=compress_level,
                            lossless=lossless)
        case _:
            log("Unknown extension type. Only supports png, jpeg, jpg, webp",t="error")
            sys.exit(1)