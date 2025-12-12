import json
import os
import sys
import colorama
colorama.init()


default_config = {
    "jpeg": {
        "quality": 75,
        "color_mode":"RGB"
    },

    "png": {
        "optimize": False,
        "compress_level": 6,
        "color_mode": "RGBA"
    },
    "webp": {
        "quality": 75,
        "lossless": False,
        "compress_level": 4,
        "color_mode": "RGBA"
    },
    "log":{
        "level": "info"
    }
}


if getattr(sys, "frozen", False):
    config_path = os.path.join(os.path.dirname(sys.executable),"config.json")
else:
    config_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"config.json")



try:
    if not os.path.exists(config_path):
        print(f"\033[33mConfig file not found at {config_path}. Making new one...\033[0m")
        with open(config_path, "w") as f:
            json.dump(default_config, f,indent=4)

    with open(config_path, "r") as f:
        json_config = json.load(f)
except FileNotFoundError:
    print(f"\033[31mConfig file not found at {config_path}\033[0m")
    sys.exit(1)
except json.decoder.JSONDecodeError as e:
    print(f"\033[31mError decoding config file at {config_path}\033[0m")
    sys.exit(1)
except Exception as e:
    print(f"\033[31mUnexpected error: {e}\033[0m")
    sys.exit(1)


class Config:
    log_level = json_config.get("log_level","info")

    class PNG:
        optimize = json_config.get("png",{}).get("optimize",False)
        compress_level = json_config.get("png",{}).get("compress_level",6)
        color_mode = json_config.get("png",{}).get("color_mode","RGBA")

    class JPEG:
        quality = json_config.get("jpeg",{}).get("quality",75)
        color_mode = json_config.get("jpeg",{}).get("color_mode","RGB")

    class WEBP:
        quality = json_config.get("webp",{}).get("quality",75)
        lossless = json_config.get("webp",{}).get("lossless",False)
        compress_level = json_config.get("webp",{}).get("compress_level",4)
        color_mode = json_config.get("webp",{}).get("color_mode","RGBA")
