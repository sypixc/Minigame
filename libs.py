import json
import os


def welcome_message(title):
    style = "*" * (len(title) + 6)
    
    print(style)
    print(f"** {title} **")
    print(style)


def loadUserData(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            return json.load(file)
    return{}

def saveUserData(fileName, data):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)