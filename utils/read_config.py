import json


def getConfig():
    with open("config.json", "r") as file:
        json_object = json.load(file)

    return json_object
