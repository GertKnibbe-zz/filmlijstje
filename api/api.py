import requests
apikey = "c2a7b567"

def run_api_request(zoekfunctie, zoekopdracht, zoektype) :

    request_url = f"http://www.omdbapi.com/?{zoekfunctie}={zoekopdracht}&type={zoektype}&apikey={apikey}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return {"success": True, "data": data}
        else:
            return {"success": False, "error": "Geen resultaten gevonden."}
    else:
        return {"success": False, "error": f"Foutcode: {response.status_code}"}