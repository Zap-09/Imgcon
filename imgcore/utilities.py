
level = "info"


def log(msg,t="info"):
    if level == "none":
        return

    if level == "--info":
        if t == "info":
            print(msg)
    elif level == "--warn":
        if t == "warn":
            print(msg)
    elif level == "--error":
        if t == "error":
            print(msg)

    log_type = []

    if level == "info":
        log_type = ["info","warn","error"]
    elif level == "warn":
        log_type = ["warn", "error"]
    elif level == "error":
        log_type = ["error"]
    if t in log_type:
        print(msg)
