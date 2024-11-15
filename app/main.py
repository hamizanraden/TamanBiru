# run.py

from cli.auth.login import start_login
from cli.auth.register import start_register

if __name__ == '__main__':
    print('┌───────────────────୨ৎ──────────────────┐')
    print('│ Selamat Datang di Aplikasi Taman Biru │')
    print('│───────────────────────────────────────│')
    print('│   Apakah kamu sudah memiliki akun?    │')
    print('│───────────────────────────────────────│')
    print('│    1. Ya, saya sudah memiliki akun    │')
    print('│  2. Tidak, saya belum memiliki akun   │')
    print('└───────────────────────────────────────┘')

# memilih jawaban 1 atau 2    
masuk = input('Pilih jawaban: ')

# kondisional untuk memilih login atau register
if masuk == '1' or 'Ya':
    start_login()
elif masuk == '2' or 'Tidak':
    start_register()