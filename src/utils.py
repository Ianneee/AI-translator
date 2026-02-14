import subprocess
import platform


def copy_to_clipboard(text):
    system = platform.system()

    if system == "Windows":
        subprocess.run("clip", input=text.strip().encode("utf-8"), check=True)

    elif system == "Darwin":
        subprocess.run("pbcopy", input=text.encode("utf-8"), check=True)

    elif system == "Linux":
        subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.encode("utf-8"),
            check=True
        )
    else:
        raise Exception("Unsupported operating system")

