import sys
import os
sys.path.append(os.path.abspath('./app/cli/chat/'))
from chat_all import chat_all
from chatProdi import program_studi
from leaderBoard import leaderboard
from main.settings import settings_menu
from chat.CekAkun import cekAkun
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
        masuk = input('Pilih menu: ').lower()

        if masuk == '1' or masuk == 'chat all':
            chat_all()
        elif masuk == '2' or masuk == 'program studi':
            program_studi()
        elif masuk == '3' or masuk == 'leaderboard':
            leaderboard()
        elif masuk == '4' or masuk == 'settings':
            settings_menu()
        elif masuk == '5' or masuk == 'cek akun':
            cekAkun()
        elif masuk == '6' or masuk == 'logout':
            print('Anda telah keluar dari akun Anda')
            break
        else:
            print('Menu tidak tersedia')
