from api import run_api_request
from utils import build_menu
from pprint import pprint

def search_menu() :
    while True:
        choice = build_menu(
            "Zoeken, kies uit onderstaande:",
            [
                "Film zoeken",
                "Serie zoeken",
                "Ga terug naar hoofdmenu"
            ]
        )

        if choice == "1":
            search_action(
                "movie",
                "films"
            )
        elif choice == "2":
            search_action(
                "series",
                "series"
            )
        elif choice == "3":
            return  # terug naar hoofdmenu
        else:
            print("Ongeldige invoer.")

def search_action(type_of, type_title) :
    while True :
        search_input = input(f"Zoeken naar {type_title} (Type 'Terug' om te stoppen): ")
        if search_input == "Terug":
            break

        result = run_api_request(
            "s",
            search_input,
            type_of
        )
        if result["success"] :
            search_results = result["data"]
            print("\nJe zoekopdracht: \"", search_input, "\" heeft", search_results["totalResults"], "resultaten:")
            print("---" * 10)
            for index, movie in enumerate(search_results["Search"], start=1) :
                print(f"{index}. {movie['Title']} ({movie['Year']})")
            print("---" * 10)

            while True :
                action = build_menu(
                "Navigatie:",
                [
                        "Film data bekijken",
                        "Opnieuw zoeken",
                        "Ga terug naar hoofdmenu"
                    ]
                )

                if action == "1" :
                    movie_selection = int(input("Voer het resultaatnummer van de film in: ")) -1
                    selected_movie = select_movie(
                        search_results["Search"][movie_selection]['imdbID'],
                        type_of
                    )
                    pprint(selected_movie["data"])

                    action = build_menu(
                        "Acties:",
                        [
                            "Film opslaan",
                            "Terug naar zoeken",
                            "Ga terug naar hoofdmenu"
                        ]
                    )

                    if action == "1" :
                        # add_to_watchlist(
                        #     toevoegen aan watchlist
                        # )
                        movie_title = selected_movie["data"]["Title"]
                        print(f"{movie_title} is opgeslagen in je watchlist!")
                    elif action == "2" :
                        return
                    elif action == "3" :
                        print("test")

                elif action == "2" :
                    break
                elif action == "3" :
                    return
                else:
                    print("Ongeldige keuze.")

        else :
            print(f"⚠️ {result['error']}")
            break

def select_movie(movie_id, type_of) :
    result = run_api_request(
        "i",
        movie_id,
        type_of
    )
    return result