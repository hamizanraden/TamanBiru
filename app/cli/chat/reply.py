
from chat.message import message

def tambah_komentar (komen):
    if komen:
        message.append(komen)
        print ("anda telah menambahkan komentar")
    else:
        print ("Tidak ada komentar")

def display_komentar ():
    if message:
        for i, komen in enumerate (message, 1):
            print (f"{i}. {komen}")
    else:
        print ("Kosong")


while True:
    print("   ┌─────────────────────┐")
    print("   |      POSTINGAN      |")
    print("   |        (´◡`)        |")
    print("   |                     |")
    print("   └1─2─3────────────────┘")

    print("\n1. Tambahkan komentar")
    print("2. Lihat komentar")
    print("3. Keluar")

    memilih = input("Masukkan pilihan: ")

    if memilih == '1':
        user_comment = input("Masukkan komentar Anda: ")
        tambah_komentar(user_comment)
    elif memilih == '2':
        display_komentar()
    elif memilih == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")