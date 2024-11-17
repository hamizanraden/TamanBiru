# Fitur Komentar belum digabung dengan data base

komentar =[]

def tambah_komentar (komen):
    if komen:
        komentar.append(komen)
        print ("anda telah menambahkan komentar")
    else:
        print ("Tidak ada komentar")

def display_komentar ():
    if komentar:
        for i, komen in enumerate (komentar, 1):
            print (f"{i}. {komen}")
    else:
        print ("Kosong")


while True:
    print("   ._____________________.")
    print("   |      POSTINGAN      |")
    print("   |        (´◡`)        |")
    print("   |                     |")
    print("   |_1_2_3_______________|")

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
