# main.py
import sys
import os
sys.path.append(os.path.abspath('./app/cli/chat/'))
from chat_all import chat_all
from chatProdi import program_studi
from leaderBoard import leaderboard
from main.settings import settings_menu

# tampilan halaman utama aplikasi
def start_lobby():
    while True:
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│               TamanBiru               │')
        print('│───────────────────────────────────────│')
        print('│ 1. 👥 Chat All                        │')
        print('│ 2. 💼 Program Studi                   │')
        print('│ 3. 🥇 Leaderboard                     │')
        print('│ 4. ⚙️  Settings                        │')
        print('│ 5. 🎭 Cek Akun                        │')
        print('│ 6. ❌ Logout                          │')
        print('│───────────────────────────────────────│')
        print('└───────────────────────────────────────┘')

# user memilih menu
        masuk = input('Pilih menu: ').lower()
# kondisional untuk memilih menu
        if masuk == '1' or masuk == 'Chat All'.lower():
            chat_all()

        elif masuk == '2' or masuk == 'Program Studi'.lower():
            program_studi()

        elif masuk == '3' or masuk == 'Leaderboard'.lower():
            leaderboard()
            
        elif masuk == '4' or masuk == 'Settings'.lower():
            settings_menu()
        
        elif masuk == '5' or masuk == 'Cek Akun'.lower():
            print('Cek Akun')

        elif masuk == '6' or masuk == 'Logout'.lower():
            print('Anda telah keluar dari akun anda')
            break
        
        else:
            print('Menu tidak tersedia')
        