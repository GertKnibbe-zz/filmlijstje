from utils import build_menu
from menus.search import search_menu

def main_menu() :
    while True :
        choice = build_menu(
            "Welkom bij jouw filmlijstje, kies uit onderstaande:",
            [
                "Film of serie zoeken op internet",
                "Bekijk/bewerk watchlist",
                "Sluit af"
            ]
        )

        if choice == "1" :
            status = search_menu()
            if status == "back_to_main":
                continue
        elif choice == "2" :
            status = search_menu()
            if status == "back_to_main":
                continue

        elif choice == "3" :
            print("App afgesloten")
            break
        else :
            print("Ongeldige input, probeer opnieuw")

if __name__ == "__main__":
    main_menu()