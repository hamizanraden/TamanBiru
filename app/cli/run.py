# main.py
import sys
import os
from auth.login import access_login
from auth.register import access_register

def logout():
    print("\nAnda telah berhasil logout.")
    print("Mengembalikan Anda ke menu utama...\n")
    display_main_menu()#agar pas logout pada main, akan break, langsung kesini

def display_main_menu():
    while True:
        print('\u250c───────────────────୨ৎ──────────────────┐')
        print('│ Selamat Datang di Aplikasi Taman Biru │')
        print('│───────────────────────────────────────│')
        print('│   Apakah kamu sudah memiliki akun?    │')
        print('│───────────────────────────────────────│')
        print('│   1. Iya, saya sudah memiliki akun    │')
        print('│  2. Tidak, saya belum memiliki akun   │')
        print('│       3. Keluar dari aplikasi         │')
        print('└───────────────────────────────────────┘')

        masuk = input('Pilih jawaban: ').strip()

        if masuk == '1' or masuk.lower() == 'iya':
            result = access_login('start_login')
            if result == 'logout':
                logout()
        elif masuk == '2' or masuk.lower() == 'tidak':
            result = access_register('start_register')
            if result == 'logout':
                logout()
        elif masuk == '3' or masuk.lower() == 'keluar':
            print('Terima kasih telah menggunakan aplikasi kami.')
            break
        else:
            print('Pilihan tidak tersedia.')

if __name__ == '__main__':
    display_main_menu()