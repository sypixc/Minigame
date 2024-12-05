import random
from libs import welcome_message


welcome_message("Selamat datang di game kami!!")




while True:
    bentukGoa = '|_|'
    goaKosong = [bentukGoa] * 4

    Xpos = random. randint(1,4)
    goa = goaKosong.copy()
    goa[Xpos - 1]= '|H|'

    goaKosong = ' '.join(goaKosong)
    goa = ' '.join(goa)

    print(f'''
    Coba perhatikan goa dibawah ini
    {goaKosong}
    ''')

    userOption = int(input('Menurut kamu goa yang isi di nomor berapa? [1-4] : '))
    if userOption == Xpos:
        print(f"\n{goa}\n Selamat tebakan kamu benar!!")
    else:
        print(f'\n{goa}\n Maaf tebakan kamu salah')

    
    playAgain = input("\n\napakah ingin lanjut main? [y/n]")
    if playAgain == 'n':
        break

print('program selesai!')