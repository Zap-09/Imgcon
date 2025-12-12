from PIL import Image
import os
from natsort import natsorted
from imgcore.utilities import log
from imgcore.config import Config


quality_warn = False
compress_level_warn = False
lossless_and_quality_warn = False


def convert_to_jpeg(image_file,
                    quality = None,
                    output_path = None,
                    color_mode = None):

    if not quality:
        quality = Config.JPEG.quality

    if not color_mode:
        color_mode = Config.JPEG.color_mode


    global quality_warn
    if not os.path.exists(image_file):
        log(f"Could not locate file: {image_file}","error")
        return


    if not color_mode in ["RGB","L"]:
        log("Unknown color mode. Please use 'RGB', 'L'",t="error")
        return

    if quality > 100:
        quality = 100
        if not quality_warn:
            log("Quality Value was set over 100. Anything above 100 is redundant. Setting quality value to 100","warn")
            quality_warn = True

    elif quality < 0:
        quality = 0
        if not quality_warn:
            log("Quality Value was set under 0. Anything under 0 is redundant. Setting quality value to 0","warn")
            quality_warn = True


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
            try:
                img.save(os.path.join(output_path,f"{base_name}.jpg"),"JPEG",quality = quality)
            except Exception as e:
                log(f"Error saving image: {e}","error")
                return
        else:
            try:
                img.save(f"{base_name}.jpg","JPEG",quality = quality)
            except Exception as e:
                log(f"Error saving image: {e}","error")
                return
        log(f"Conversion complete: {os.path.join(output_path,base_name)}.jpg",t="info")



def convert_to_png(image_file,
                   output_path = None,
                   color_mode = None,
                   optimize = False,
                   compress_level = None):

    if not compress_level:
        compress_level = Config.PNG.compress_level

    if not optimize:
        optimize = Config.PNG.optimize

    if not color_mode:
        color_mode = Config.PNG.color_mode


    global compress_level_warn

    if not os.path.exists(image_file):
        log(f"Could not locate file: {image_file}","error")
        return

    if not color_mode in ["RGBA","RGB","L"]:
        log("Unknown color mode. Please use 'RGBA', 'RGB', 'L'",t="error")
        return
    if compress_level > 9:
        compress_level = 9
        if not compress_level_warn:
            log("Compress level was set over 9. Anything above 9 is redundant. Setting Compress level to 9", "warn")
            compress_level_warn = True

    elif compress_level < 0:
        compress_level = 0
        if not compress_level_warn:
            log("Compress level was set under 0. Anything under 0 is redundant. Setting Compress level to 0", "warn")
            compress_level_warn = True

    try:
        with Image.open(image_file) as img:
            img = img.convert(color_mode)
    except:
        log(f"Invalid color mode","error")


        file_name = os.path.basename(image_file)
        base_name, _ = os.path.splitext(file_name)
        if output_path:
            try:
                os.makedirs(output_path,exist_ok=True)
            except:
                log("Invalid file path",t="error")
                return
            try:
                img.save(os.path.join(output_path,f"{base_name}.png"),"PNG",optimize=optimize, compress_level=compress_level)
            except Exception as e:
                log(f"Error saving image: {e}","error")
                return
        else:
            try:
                img.save(f"{base_name}.png",optimize=optimize, compress_level=compress_level)
            except Exception as e:
                log(f"Error saving image: {e}","error")
                return
        log(f"Conversion complete: {os.path.join(output_path,base_name)}.png",t="info")



def convert_to_webp(image_file,
                    output_path = None,
                    color_mode = None,
                    quality = None,
                    lossless = False,
                    compress_level = None):

    if not color_mode:
        color_mode = Config.WEBP.color_mode

    if not quality:
        quality = Config.WEBP.quality

    if not lossless:
        lossless = Config.WEBP.lossless

    if not compress_level:
        compress_level = Config.WEBP.compress_level

    global quality_warn
    global compress_level_warn
    global lossless_and_quality_warn


    if not os.path.exists(image_file):
        log(f"Could not locate file: {image_file}","error")
        return


    if not color_mode in ["RGBA","RGB","LA","L"]:
        log("Unknown color mode. Please use 'RGBA', 'RGB', 'L', 'LA'",t="error")
        return


    if quality and lossless:
        quality = None
        if not lossless_and_quality_warn:
            log("Both Quality and Lossless parameters are set to true. So Quality parameters will be ignored","warn")
            lossless_and_quality_warn = True

    if quality and not lossless:
        if quality > 100:
            quality = 100
            if not quality_warn:
                log("Quality Value was set over 100. Anything above 100 is redundant. Setting quality value to 100", "warn")
                quality_warn = True
        elif quality < 0:
            quality = 0
            if not quality_warn:
                log("Quality Value was set under 0. Anything under 0 is redundant. Setting quality value to 0","warn")
                quality_warn = True

    if compress_level > 6:
        compress_level = 6
        if compress_level_warn:
            log("Compress level was set over 6. Anything above 6 is redundant. Setting Compress level to 6", "warn")

    elif compress_level < 0:
        compress_level = 0
        if compress_level_warn:
            log("Compress level was set under 0. Anything under 0 is redundant. Setting Compress level to 0", "warn")


    with Image.open(image_file) as img:
        try:
            img.convert(color_mode)
        except:
            log(f"Invalid color mode","error")

        file_name = os.path.basename(image_file)
        base_name, _ = os.path.splitext(file_name)
        if output_path:
            try:
                os.makedirs(output_path, exist_ok=True)
            except:
                log("Invalid file path", t="error")
                return
            try:
                if quality:
                    img.save(os.path.join(output_path,f"{base_name}.webp"),"WEBP",quality = quality,lossless = lossless,method = compress_level)
                else:
                    img.save(os.path.join(output_path,f"{base_name}.webp"),"WEBP",lossless = lossless,method = compress_level)
            except Exception as e:
                log(f"Error saving image: {e}","error")
                return
        else:
            try:
                if quality:
                    img.save(f"Conversion complete {base_name}.webp","WEBP",quality = quality,lossless = lossless,method = compress_level)
                else:
                    img.save(f"{base_name}.webp","WEBP",lossless = lossless,method = compress_level)
            except Exception as e:
                log(f"Error saving image: {e}","error")
                return

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
