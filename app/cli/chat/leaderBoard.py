import os

def readUser():
    if not os.path.exists('./app/cli/data/logindatabase.txt'):
        return []
    with open('./app/cli/data/logindatabase.txt', 'r', encoding='utf-8') as file:
        return file.readlines()

def listUser():
    users = readUser()
    if not users:
        print('\n Tidak ada user.')
    else:
        print('\nUser yang terdaftar:')
        for i, user in enumerate(users, 1):
            print(f'👤 {user.strip().split(",")[0]}')

def leaderboard():
    while True:
        print('\n┌───────────────────୨ৎ────────────────────┐')
        print('│               Leaderboard               │')
        print('│─────────────────────────────────────────│')
        print('│ 1. 📜 Lihat User                        │')
        print('│ 2. 🔙 Kembali                           |')
        print('└─────────────────────────────────────────┘')
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            listUser()
        elif pilihan == "2":
            print('Kembali ke menu utama...')
            break
        else:
            print('Pilihan tidak valid.')