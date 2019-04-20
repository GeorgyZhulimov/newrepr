import requests, random, json
def get_seggests(user_storage):
    if "suggest" in user_storage.keys():
        suggest = []
        for suggest in user_storage["suggest"]:
            suggest.append({"title" : suggest, "hide": True})
        else:
            suggest = []
            return suggest, user_storage

def read_data(name:str) -> dict:
    return json.load(open(name + ".json", encoding="utf-8"))

def message_return(response, user_storage, message):
    response.set_text(message)
    response.set_tts(message)
    buttons, user_storage = get_seggests(user_storage)
    response.set_buttons(buttons)
    return response, user_storage

def message_error(response, user_storage, answer):
    message = random.choice(["Я тебя не поняла,повтори,пожалуйста."])
    return message_return(response, user_storage, message)
