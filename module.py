import random

def welcome_message(title):
    style = "*" * (len(title) + 6)
    
    print(style)
    print(f"** {title} **")
    print(style)

welcome_message("Selamat datang di game kami!!")

def levOption():
    levOption = input("Pilih level [1-3] : ")
    if levOption == "1":
        lev1()
    elif levOption =="2":
        lev2()
    elif levOption == "3":
        lev3()



def lev1():
    while True:
        bentukGoa = '|_|'
        goaKosong = [bentukGoa] * 4

        Xpos = random. randint(1,4)
        goa = goaKosong.copy()
        goa[Xpos - 1]= '|H|'

        goaKosong = ' '.join(goaKosong)
        goa = ' '.join(goa)

        print(f"\nCoba perhatikan goa ini \n {goaKosong}")

        userOption = int(input('Menurut kamu goa yang isi di nomor berapa? [1-4] : '))
        if userOption == Xpos:
            print(f"\n{goa}\n Selamat tebakan kamu benar!!")
        else:
            print(f'\n{goa}\n Maaf tebakan kamu salah')

        
        playAgain = input("\n\napakah ingin lanjut main? [y/n] : ")
        if playAgain == "y":
            levOption()
        else:
            break

    print('program selesai!')

def lev2():
    while True:
        bentukGoa = '|_|'
        goaKosong = [bentukGoa] * 6

        Xpos = random. randint(1,6)
        goa = goaKosong.copy()
        goa[Xpos - 1]= '|H|'

        goaKosong = ' '.join(goaKosong)
        goa = ' '.join(goa)

        print(f"\nCoba perhatikan goa ini \n {goaKosong}")

        userOption = int(input('Menurut kamu goa yang isi di nomor berapa? [1-6] : '))
        if userOption == Xpos:
            print(f"\n{goa}\n Selamat tebakan kamu benar!!")
        else:
            print(f'\n{goa}\n Maaf tebakan kamu salah')

        
        playAgain = input("\n\napakah ingin lanjut main? [y/n] : ")
        if playAgain == 'y':
            levOption()
        else:
            break

    print('program selesai!')

def lev3():
    while True:
        bentukGoa = '|_|'
        goaKosong = [bentukGoa] * 8

        Xpos = random. randint(1,8)
        goa = goaKosong.copy()
        goa[Xpos - 1]= '|H|'

        goaKosong = ' '.join(goaKosong)
        goa = ' '.join(goa)

        print(f"\nCoba perhatikan goa ini \n {goaKosong}")

        userOption = int(input('Menurut kamu goa yang isi di nomor berapa? [1-8] : '))
        if userOption == Xpos:
            print(f"\n{goa}\n Selamat tebakan kamu benar!!")
        else:
            print(f'\n{goa}\n Maaf tebakan kamu salah')

        
        playAgain = input("\n\napakah ingin lanjut main? [y/n] : ")
        if playAgain == 'y':
            levOption
        elif playAgain == "n":
            break

    print('program selesai!')

levOption()