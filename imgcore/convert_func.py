from PIL import Image
import os
from natsort import natsorted
from imgcore.utilities import log


def convert_to_jpeg(image_file,
                    quality = None,
                    output_path = None,
                    color_mode = None):


    if not os.path.exists(image_file):
        log(f"Could not locate file: {image_file}","error")
        return

    if quality is None:
        quality = 75

    if color_mode is None:
        color_mode = "RGB"

    if not color_mode in ["RGB","L"]:
        log("Unknown color mode. Please use 'RGB', 'L'",t="error")
        return

    if quality > 100:
        log("Quality Value was set over 100. Anything above 100 is redundant. Setting quality value to 100","warn")
        quality = 100

    elif quality < 0:
        log("Quality Value was set under 0. Anything under 0 is redundant. Setting quality value to 0","warn")
        quality = 0

    with Image.open(image_file) as img:
        img = img.convert(color_mode)

        file_name = os.path.basename(image_file)
        base_name, _ = os.path.splitext(file_name)

        if output_path:
            try:
                os.makedirs(output_path,exist_ok=True)
            except:
                log("Invalid file path",t="error")
                return
            img.save(os.path.join(output_path,f"{base_name}.jpg"),"JPEG",quality = quality)
        else:
            img.save(f"{base_name}.jpg","JPEG",quality = quality)
        log(f"Conversion complete: {os.path.join(output_path,base_name)}.jpg",t="info")



def convert_to_png(image_file,
                   output_path = None,
                   color_mode = None,
                   optimize=False,
                   compress_level=None):

    if not os.path.exists(image_file):
        log(f"Could not locate file: {image_file}","error")
        return

    if optimize is None:
        optimize = False

    if compress_level is None:
        compress_level = 6

    if color_mode is None:
        color_mode = "RGBA"

    if not color_mode in ["RGBA","RGB","L"]:
        log("Unknown color mode. Please use 'RGBA', 'RGB', 'L'",t="error")
        return
    if compress_level > 9:
        log("Compress level was set over 9. Anything above 9 is redundant. Setting Compress level to 9", "warn")
        compress_level = 9

    elif compress_level < 0:
        log("Compress level was set under 0. Anything under 0 is redundant. Setting Compress level to 0", "warn")
        compress_level = 0

    with Image.open(image_file) as img:
        img = img.convert(color_mode)

        file_name = os.path.basename(image_file)
        base_name, _ = os.path.splitext(file_name)

        if output_path:
            try:
                os.makedirs(output_path,exist_ok=True)
            except:
                log("Invalid file path",t="error")
                return
            img.save(os.path.join(output_path,f"{base_name}.png"),"PNG",optimize=optimize, compress_level=compress_level)
        else:
            img.save(f"{base_name}.png",optimize=optimize, compress_level=compress_level)
        log(f"Conversion complete: {os.path.join(output_path,base_name)}.png",t="info")



def convert_to_webp(image_file,
                    output_path = None,
                    color_mode = None,
                    quality = None,
                    lossless = False,
                    compress_level = None):

    if not os.path.exists(image_file):
        log(f"Could not locate file: {image_file}","error")
        return

    if color_mode is None:
        color_mode = "RGBA"

    if not color_mode in ["RGBA","RGB","LA","L"]:
        log("Unknown color mode. Please use 'RGBA', 'RGB', 'L', 'LA'",t="error")
        return

    if quality is None:
        quality = 75

    if compress_level is None:
        compress_level = 4

    if lossless and quality == 75:
        quality = None

    if quality and lossless:
        log("Both Quality and Lossless parameters are set to true. So Quality parameters will be ignored","warn")
        quality = None


    if quality and not lossless:
        if quality > 100:
            log("Quality Value was set over 100. Anything above 100 is redundant. Setting quality value to 100", "warn")
            quality = 100

        elif quality < 0:
            log("Quality Value was set under 0. Anything under 0 is redundant. Setting quality value to 0", "warn")
            quality = 0

    if compress_level > 6:
        log("Compress level was set over 6. Anything above 6 is redundant. Setting Compress level to 6", "warn")
        compress_level = 6

    elif compress_level < 0:
        log("Compress level was set under 0. Anything under 0 is redundant. Setting Compress level to 0", "warn")
        compress_level = 0


    with Image.open(image_file) as img:
        img.convert(color_mode)
        file_name = os.path.basename(image_file)
        base_name, _ = os.path.splitext(file_name)

        if output_path:
            try:
                os.makedirs(output_path, exist_ok=True)
            except:
                log("Invalid file path", t="error")
                return
            if quality:
                img.save(os.path.join(output_path,f"{base_name}.webp"),"WEBP",quality = quality,lossless = lossless,method = compress_level)
            else:
                img.save(os.path.join(output_path,f"{base_name}.webp"),"WEBP",lossless = lossless,method = compress_level)
        else:
            if quality:
                img.save(f"Conversion complete {base_name}.webp","WEBP",quality = quality,lossless = lossless,method = compress_level)

            else:
                img.save(f"{base_name}.webp","WEBP",lossless = lossless,method = compress_level)
        log(f"Conversion complete: {os.path.join(output_path,base_name)}.webp",t="info")



def get_nested_file_paths(folder_path):
    extensions = (".png",".jpg",".jpeg",".webp")
    file_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file_path.casefold().endswith(ext) for ext in extensions):
                file_paths.append(file_path)

    return natsorted(file_paths)



def get_files_from_folder(folder_path):
    extensions = (".png", ".jpg", ".jpeg", ".webp")
    file_paths = []

    for items in os.listdir(folder_path):
        file_path = os.path.join(folder_path,items)

        if os.path.isfile(file_path) and any(file_path.casefold().endswith(ext) for ext in extensions):
            file_paths.append(file_path)

    return natsorted(file_paths)



def convert_folder(folder_path,ext:str,nested_folder:bool = False,**kwargs):
    ext = ext.lower()
    if nested_folder:
        all_image_path = get_nested_file_paths(folder_path)
    else:
        all_image_path = get_files_from_folder(folder_path)

    output_path = kwargs.get("output_path", folder_path)

    for image in all_image_path:

        relative_path = str(os.path.relpath(image, folder_path))
        output_image_path = os.path.join(output_path, relative_path)
        output_folder = os.path.dirname(output_image_path)


        png_kwargs = {key: value for key, value in kwargs.items() if key in ["compress_level", "optimize",]}

        jpeg_kwargs = {key: value for key, value in kwargs.items() if key in ["quality"]}

        webp_kwargs = {key: value for key, value in kwargs.items() if key in ["quality", "lossless","compress_level"]}

        match ext:
            case "png":
                convert_to_png(image,output_path=output_folder,**png_kwargs)
            case "jpg" | "jpeg":
                convert_to_jpeg(image,output_path=output_folder, **jpeg_kwargs)
            case "webp":
                convert_to_webp(image,output_path=output_folder, **webp_kwargs)
            case _:
                log("Unknown extension type. Only supports png, jpeg, jpg, webp", t="error")
