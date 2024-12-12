# main.py

from chat.reply import *

# tampilan halaman utama aplikasi
def start_lobby():
    while True:
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│               TamanBiru               │')
        print('│───────────────────────────────────────│')
        print('│ 1. 👥 Chat All                        │')
        print('│ 2. 💼 Program Studi                   │')
        print('│ 3. 🥇 Leaderboard                     │')
        print('│ 4. 👤 Cek Akun                        │')
        print('│ 5. ❌ Logout                          │')
        print('│───────────────────────────────────────│')
        print('└───────────────────────────────────────┘')

# user memilih menu
        masuk = input('Pilih menu: ')

# kondisional untuk memilih menu
<<<<<<< HEAD
        if masuk == '1' or masuk == 'Chat All'.lower:
            print('Chat All')
=======
        if masuk == '1' or masuk == 'Chat All'.lower():
            print('start_message')
>>>>>>> radenwork
            break
        elif masuk == '2' or masuk == 'Program Studi'.lower():
            print('Program Studi')
            
<<<<<<< HEAD
        elif masuk == '3' or masuk == 'Leaderboard'.lower:
            print('Leaderboard')
            
        elif masuk == '4' or masuk == 'Cek Akun'.lower:
            print('Cek Akun')
            
        elif masuk == '5' or masuk == 'Logout'.lower:
=======
        elif masuk == '3' or masuk == 'Mata Kuliah'.lower():
            print('Mata Kuliah')
            
        elif masuk == '4' or masuk == 'Leaderboard'.lower():
            print('Leaderboard')
            
        elif masuk == '5' or masuk == 'Cek Akun'.lower():
            print('Cek Akun')
            
        elif masuk == '6' or masuk == 'Logout'.lower():
>>>>>>> radenwork
            print('Anda telah keluar dari aplikasi')
            break

        else:
            print('Menu tidak tersedia')
        