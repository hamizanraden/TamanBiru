# main.py

from cli.chat.message import access_message

# tampilan halaman utama aplikasi
def start_lobby():
    while True:
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│               TamanBiru               │')
        print('│───────────────────────────────────────│')
        print('│ 1. 👥 Chat All                        │')
        print('│ 2. 💼 Program Studi                   │')
        print('│ 3. 📚 Mata Kuliah                     │')
        print('│ 4. 🥇 Leaderboard                     │')
        print('│ 5. 👤 Cek Akun                        │')
        print('│ 6. ❌ Logout                          │')
        print('│───────────────────────────────────────│')
        print('└───────────────────────────────────────┘')

# user memilih menu
        masuk = input('Pilih menu: ')

# kondisional untuk memilih menu
        if masuk == '1' or masuk == 'Chat All'.lower:
            access_message('start_message')
            break
        elif masuk == '2' or masuk == 'Program Studi'.lower:
            print('Program Studi')
            
        elif masuk == '3' or masuk == 'Mata Kuliah'.lower:
            print('Mata Kuliah')
            
        elif masuk == '4' or masuk == 'Leaderboard'.lower:
            print('Leaderboard')
            
        elif masuk == '5' or masuk == 'Cek Akun'.lower:
            print('Cek Akun')
            
        elif masuk == '6' or masuk == 'Logout'.lower:
            print('Anda telah keluar dari aplikasi')
            break

        else:
            print('Menu tidak tersedia')
        