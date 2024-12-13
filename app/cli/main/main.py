# main.py

from chat.reply import *

# tampilan halaman utama aplikasi
def start_lobby():
    while True:
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│ Selamat Datang di Aplikasi Taman Biru │')
        print('│───────────────────────────────────────│')
        print('│   Apakah kamu sudah memiliki akun?    │')
        print('│───────────────────────────────────────│')
        print('│   1. Iya, saya sudah memiliki akun    │')
        print('│  2. Tidak, saya belum memiliki akun   │')
        print('│       3. Keluar dari aplikasi         │')
        print('└───────────────────────────────────────┘')

# user memilih menu
        masuk = input('Pilih menu: ')

# kondisional untuk memilih menu
        if masuk == '1' or masuk == 'Chat All'.lower:
            print('Chat All')
            break
        elif masuk == '2' or masuk == 'Program Studi'.lower:
            print('Program Studi')
            
        elif masuk == '3' or masuk == 'Leaderboard'.lower:
            print('Leaderboard')
            
        elif masuk == '4' or masuk == 'Cek Akun'.lower:
            print('Cek Akun')
            
        elif masuk == '5' or masuk == 'Logout'.lower:
            print('Anda telah keluar dari aplikasi')
            break
        else:
            print('Pilihan tidak tersedia.')

# Menjalankan aplikasi
if __name__ == '__main__':
    main()
