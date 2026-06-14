import requests


def fetch_breweries():
    """
    Fetch brewery data from Open Brewery DB API.
    """

    url = "https://api.openbrewerydb.org/v1/breweries"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

    except Exception as e:
        print("Error fetching data:", e)

    return []


def brewery_generator(breweries):
    """
    Generator function that yields breweries one by one.
    """

    for brewery in breweries:
        yield brewery