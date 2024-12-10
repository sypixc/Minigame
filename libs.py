import json
import os


def welcome_message(title):
    style = "*" * (len(title) + 6)
    
    print(style)
    print(f"** {title} **")
    print(style)

def profil():
    print("NO| Nama Anggota       | NIM:     |")
    print("1 | Yuhansen Yordania  | 15240358 |")
    print("2 | Ariyo Baskoro      |          |")
    print("3 | Abyan Anjay Mabar  |          |")
    print("4 | Hendri Ahmad       | 15240019 |")

def loadUserData(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            return json.load(file)
    return{}

def saveUserData(fileName, data):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)