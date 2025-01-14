import os
from auth.share import get_nama_pengguna

def getUser():
    if not os.path.exists('./app/cli/data/logindatabase.txt'):
        return []
    with open('./app/cli/data/logindatabase.txt', 'r', encoding='utf-8') as file:
        return file.readlines()
    
def displayLoggedInUser(username):
    users = getUser()
    for user in users:
        user_info = user.strip().split(',')
        if user_info[0] == username:
            print(f"\nInformasi Akun:")
            print(f"Username : {user_info[0]}")
            print(f"Email    : {user_info[1]}")
            print(f"Prodi    : {user_info[3] if len(user_info) > 3 else 'Tidak tersedia'}")
            print(f"No Telp  : {user_info[5] if len(user_info) > 5 else 'Tidak tersedia'}")
            return
    
    print(f"User dengan username '{username}' tidak ditemukan.")

def cekAkun():
    nama_pengguna = get_nama_pengguna()
    if not nama_pengguna:
        print("Belum ada user yang login. Silakan login terlebih dahulu.")
        return
    
    while True:
        print('\n┌───────────────────୨ৎ─────────────────────┐')
        print('│                  Cek Akun                 │')
        print('│───────────────────────────────────────────│')
        print('│ 1. 📜 Tampilkan Informasi Akun            │')
        print('│ 2. 🔙 Kembali                             │')
        print('└───────────────────────────────────────────┘')
        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == "1" :
            displayLoggedInUser(nama_pengguna)
        elif pilihan == "2":
            print('Kembali ke menu utama...')
            break
        else:
            print('Pilihan tidak valid.')
