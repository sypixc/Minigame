import random
import json
import os

def loadUserData(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            return json.load(file)
    return{}

def saveUserData(fileName, data):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)

def game():
    fileName = "userData.json"
    userData = loadUserData(fileName)

    print("Selamat datang di Minigame kami!!")
    userName = input("Masukkan nama kamu : ").strip()

    if userName in userData:
        total = userData[userName]
        print(f"Selamat datang kembali, {userName}! Credit anda : {total}")
    else:
        print(f"Profil baru dibuat untuk {userName}!!")
        total = 120

    game = "Y"

    while (game == "Y" or game == "y"):
        print (" Anda memiliki : ", total, "Credit")
        
        while True:
            bbet=int(input("Mau bet berapa?? (Kelipatan 10) : "))
            try:
                bet = int(bbet)
                if bet>total:
                    print("Ga cukup creditnya cuy!!")
                elif bet % 10 != 0:
                    print("Harus kelipatan 10!!")
                else: 
                    break
            except ValueError:
                print("Angka ga valid!!")

        bentukGoa = '|_|'
        goaKosong = [bentukGoa] * 4

        Xpos = random. randint(1,4)
        goa = goaKosong.copy()
        goa[Xpos - 1]= '|H|'

        goaKosong = ' '.join(goaKosong)
        goa = ' '.join(goa)

        print(f"\nCoba perhatikan goa ini \n {goaKosong}")

        guess = int(input('Menurut kamu goa yang isi di nomor berapa? [1-4] : '))

        while guess > 4:
            print("Kelebihan bre!!")
            guess = int(input("Menurut kamu goa yang isi di nomor berapa? [1-4] : "))
        print(f"\n {goa}\n")

        if bet <= 50 :
            multi = 1.0
        elif bet <= 100 :
            multi = 1.5
        elif bet <= 200 :
            multi = 2.0
        else:
            multi = 3.0


        if Xpos != guess:
            print("Kamu kalah")
            total -= bet
        else:
            poin = int(bet * multi)
            print(f"Selamat kamu benar!! Kamu mendapat {poin} poin !!")
            total+=poin
        
        if total<=0:
            input("Credit mu abis bre, tekan enter buat keluar")
            del userData[userName]
            saveUserData(fileName, userData)
            break
        game = input("Mau Main lagi?? [Y/N] : ").strip().upper()

        if game=="N":
            print("Total akhir : ",total, "credit")
            input("Makasih udah maen :), tekan enter untuk keluar ")
        
        userData[userName] = total
        saveUserData(fileName, userData)
game()