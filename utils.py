import os
import platform

def clear_console():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            if "TERM" in os.environ:
                os.system("clear")
            else:
                print("\n" * 100)
    except Exception:
        print("\n" * 100)
