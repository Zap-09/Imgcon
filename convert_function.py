import sys
import os
import PIL
from PIL import Image

supported_ext = ("png","jpg","jpeg","webp")

def file_exists(file_path):
    return os.path.exists(file_path)


def get_valid_file_name(input_file,ext):
    if not ext.lower() in supported_ext:
        print(f"'{ext}' is not is the supported list")
        return None
    parts = input_file.rsplit(".", 1)
    new_file = f"{parts[0]}.{ext}"
    return new_file

def list_image_files_from_dir(folder_path = None):

    if os.path.isfile(folder_path):
        return [folder_path]

    if folder_path:
        try:
            files = [folder_path+"/"+f for f in os.listdir(folder_path) if
                     os.path.isfile(os.path.join(folder_path, f)) and f.endswith(supported_ext)]
            return files
        except FileNotFoundError:
            print("Could not find the folder path")

        except Exception as e:
            print(e)
    else:
        try:
            files = [f for f in os.listdir(folder_path) if
                     os.path.isfile(f) and f.endswith(supported_ext)]
            return files
        except Exception as e:
            print(e)



def convert_image(input_image, ext:str, output_path = None):
    if not file_exists(input_image):
        print(f"File '{input_image}' not found")
        return
    if output_path:
        os.makedirs(output_path,exist_ok=True)

    if ext.lower() in supported_ext:

        output_image = os.path.basename(input_image)
        parts = output_image.rsplit(".",1)
        output_image = f"{parts[0]}.{ext}"

        if output_path:
            try:
                with Image.open(input_image) as img:
                    img.save(f"{output_path}/{output_image}",ext)
            except PIL.UnidentifiedImageError as e:
                print(e)
            except Exception as e:
                print(e)
        else:
            try:
                with Image.open(input_image) as img:
                    img.save(output_image,ext)
            except PIL.UnidentifiedImageError as e :
                print(e)
            except Exception as e:
                print(e)



def main(ext,image_folder = None,output_folder = None):
    image_file_list = list_image_files_from_dir(image_folder)
    if not image_folder:
        print(f"No image files that ware in the supported list were found. {supported_ext}")
        sys.exit()

    for file in image_file_list:
        convert_image(file,ext,output_folder)
