from libs import welcome_message, profil
from level import game

welcome_message("Selamat datang di game kami!!")

pilih=int(input("1 : Profil, 2 : Game, 3 : keluar"))
if pilih == 1:
    profil()
elif pilih == 2:
    game()
elif pilih == 3:
    exit
else:
    print("Pilih yang tersedia!!")
    exit
