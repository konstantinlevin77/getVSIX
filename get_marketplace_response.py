import requests


from get_value_from_config import get_value_from_config

def get_marketplace_response(search_term):
    
    sort_by = get_value_from_config("SortBy")

    if sort_by==None:
        return None
    
    LINK = f"https://marketplace.visualstudio.com/search?term={search_term}&target=VSCode&category=All%20categories&sortBy={sort_by}"

    response = requests.get(LINK)

    if response.status_code == 200:
        return response.text

    else:
        raise ReferenceError("Something went wrong and response's status code has been something else than 200.")