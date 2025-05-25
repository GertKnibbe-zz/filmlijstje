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

def build_menu(title, options) :
    print(title)
    print("---" * 10)
    for i, option in enumerate(options, start=1):
        print(f"  {i}) {option}")
    print("---" * 10)
    choice_user = input("Wat wil je doen? ")
    return choice_user