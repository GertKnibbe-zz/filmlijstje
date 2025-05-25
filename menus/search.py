from api.search_api import run_api_request

def run_search_menu():
    while True:

        menu = """
Zoeken naar films, kies uit onderstaande:
    1) Film zoeken
    2) Serie zoeken
    3) Ga terug naar hoofdmenu
            
Naar welk menu wil je navigeren?  """

        keuzemenu = input(menu)

        if keuzemenu == "1":
            zoektype = "movie"
            zoekopdracht = input("Zoeken naar films: ")
            resultaat = run_api_request(zoekfunctie = "s", zoekopdracht = zoekopdracht, zoektype = zoektype)
            if resultaat["success"]:
                for index, movie in enumerate(resultaat["data"]["Search"], start = 1):
                    print(f"{index}. {movie['Title']} ({movie['Year']})")
            else:
                print(f"⚠️ {resultaat['error']}")
            input("Resultaat bekijken of terug naar hoofdmenu? ")
        elif keuzemenu == "2":
            zoektype = "series"
            zoekopdracht = input("Zoeken naar series: ")
            resultaat = run_api_request(zoekfunctie="s", zoekopdracht=zoekopdracht, zoektype=zoektype)
            if resultaat["success"]:
                for movie in resultaat["data"]["Search"]:
                    print(f"📺 Titel: {movie['Title']} · Datum: {movie['Year']}")
            else:
                print(f"⚠️ {resultaat['error']}")
        elif keuzemenu == "3":
            break
        else :
            print("Incorrecte input, graag kiezen uit 1 van de 3 menu items.\n")