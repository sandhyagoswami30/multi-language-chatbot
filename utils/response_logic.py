import json


def get_response(query, language):
    with open("data/responses.json", "r", encoding="utf-8") as file:
        response = json.load(file)

    normalized_query = query.lower()
    if normalized_query in response:
        return response[normalized_query].get(language, response[normalized_query]["en"])
    else:
        return "Sorry, I didn't understand that."