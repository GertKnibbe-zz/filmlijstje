import os
import json
from utils import build_menu

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVED_DIR = os.path.join(BASE_DIR, "..", "saved")

if not os.path.exists(SAVED_DIR):
    os.makedirs(SAVED_DIR)

def watchlist_menu() :
    while True :
        check = check_for_watchlist()
        if check == "No-wishlist":
            print("Terugkeren naar het hoofdmenu...")
            return
        choice = build_menu(
            "Opties:",
            [
                "Watchlist bekijken",
                "Watchlist aanmaken",
                "Ga terug naar hoofdmenu"
            ]
        )
        if choice == "1" :
            print("kan nog niet")
        elif choice == "2" :
            create_watchlist()
        elif choice == "3" :
            break
        else :
            print("Ongeldige input probeer opnieuw")

def create_watchlist() :
    while True :
        watchlist_name = input("Hoe wil je de watchlist noemen? (maximaal 15 tekens) ")
        if len(watchlist_name) > 15 :
            print("Je watchlist naam is te lang")
        file_name = watchlist_name.strip().lower()
        file_path = os.path.join(SAVED_DIR, f"{file_name}.json")
        try:
            with open(file_path, "x") as f:
                json.dump({
                    "naam": watchlist_name,
                    "items": []
                }, f, indent=4)
            print(f"Watchlist '{watchlist_name}' is succesvol aangemaakt!")
            break
        except FileExistsError:
            print(f"Er bestaat al een watchlist met de naam '{file_name}'. Kies een andere naam.")


def check_for_watchlist() :

    if not os.path.exists(SAVED_DIR):
        print("Er zijn nog geen watchlists.")
        return

    bestanden = os.listdir(SAVED_DIR)
    watchlist_namen = []

    for bestand in bestanden:
        if bestand.endswith(".json"):
            pad = os.path.join(SAVED_DIR, bestand)
            try:
                with open(pad, "r") as f:
                    data = json.load(f)
                    naam = data.get("naam", "[naam ontbreekt]")
                    watchlist_namen.append(naam)
            except Exception as e:
                print(f"Fout bij lezen van {bestand}: {e}")

    if watchlist_namen :
        print("Je hebt watchlists:")

        for index, naam in enumerate(watchlist_namen, start=1):
            print(f"{index}. {naam}")

    else:
        print("Je hebt nog geen watchlists, wil je er een aanmaken?")
        create_dir = input("Ja of Nee? ").strip().lower()
        if create_dir == "ja":
            create_watchlist()
            return check_for_watchlist()
        elif create_dir == "nee":
            return "No-wishlist"
        else:
            return []