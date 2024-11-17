
import message

def tambah_balasan (balas):
    if balas:
        message.append(balas)
        print ("anda telah menambahkan komentar")
    else:
        print ("Tidak ada komentar")

def display_balasan ():
    if message:
        for i, balas in enumerate (message, 1):
            print (f"{i}. {balas}")
    else:
        print ("Kosong")


while True:
    print("   ┌─────────────────────┐")
    print("   |      POSTINGAN      |")
    print("   |                     |")
    print("   |                     |")
    print("   └1─2─3────────────────┘")

    print("\n1. Reply postingan")
    print("2. Lihat reply")
    print("3. Keluar")

    memilih = input("Masukkan pilihan: ")

    if memilih == '1':
        user_comment = input("Masukkan reply Anda: ")
        tambah_balasan(user_comment)
    elif memilih == '2':
        display_balasan()
    elif memilih == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")