from menus.search import run_search_menu
from utils import clear_console

def main_menu() :
    while True :
        menu ="""
Welkom bij jouw filmlijstje, kies uit onderstaande:
        
    1) Film of serie zoeken op internet
    2) Bekijk/bewerk watchlist
    3) Sluit af
        
Naar welk menu wil je navigeren?  """

        user_input = input(menu)
        if user_input == "1" :
            clear_console()
            run_search_menu()
        elif user_input == "3" :
            print("App afgesloten")
            break
        else :
            print("Ongeldige input, probeer opnieuw")



if __name__ == "__main__":
    main_menu()