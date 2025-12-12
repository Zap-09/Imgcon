import platform
import subprocess
import colorama
colorama.init()


from imgcore.config import Config

level = Config.log_level


def log(msg, t="info"):
    valid_level = ["info", "warn", "error","--info","--warn","--error"]
    if not t in valid_level:
        print(f"'{t}' is not a valid log level. Use one of the in '{valid_level}'")

    if level == "none":
        return

    reset_color = "\033[0m"
    info_color = "\033[32m"
    warn_color = "\033[33m"
    error_color = "\033[31m"


    if level == "--info":
        if t == "info":
            print(f"{info_color}{msg}{reset_color}")
    elif level == "--warn":
        if t == "warn":
            print(f"{warn_color}{msg}{reset_color}")
    elif level == "--error":
        if t == "error":
            print(f"{error_color}{msg}{reset_color}")

    log_type = []

    if level == "info":
        log_type = ["info", "warn", "error"]
    elif level == "warn":
        log_type = ["warn", "error"]
    elif level == "error":
        log_type = ["error"]
    if t in log_type:
        if t == "info":
            print(f"{info_color}{msg}{reset_color}")
        elif t == "warn":
            print(f"{warn_color}{msg}{reset_color}")
        elif t == "error":
            print(f"{error_color}{msg}{reset_color}")


def open_file_with_default_app(file_path):
    if platform.system() == "Windows":
        subprocess.Popen(["start", file_path],shell=True)