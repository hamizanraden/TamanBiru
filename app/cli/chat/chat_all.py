import os
from report.report import report_message
from auth.share import get_nama_pengguna

def read_chat():
    if not os.path.exists('./app/cli/data/chatAll.txt'):
        return []
    with open('./app/cli/data/chatAll.txt', 'r', encoding='utf-8') as file:
        return file.readlines()
    
def write_chat(message):
    with open('./app/cli/data/chatAll.txt', 'a', encoding='utf-8') as file:
        file.write(message + '\n')

def chat_all():
    while True:
        print('\n┌───────────────────୨ৎ──────────────────┐')
        print('│               Chat All                │')
        print('│───────────────────────────────────────│')
        print('│ 1. 📜 Lihat Pesan                     │')
        print('│ 2. ✍️  Kirim Pesan                     │')
        print('│ 3. ❗ Laporkan Pesan                  │')
        print('│ 4. 🔙 Kembali                         │')
        print('└───────────────────────────────────────┘')

        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            messages = read_chat()
            if not messages:
                print('\nBelum ada pesan.')
            else:
                print('\nPesan Tersimpan:')
                for idx, message in enumerate(messages, start=1):
                    print(f'{idx}. {message.strip()}')

        elif pilihan == '2':
            nama_pengguna = get_nama_pengguna()
            if not nama_pengguna:
                print('Nama pengguna tidak valid.')
                continue

            content = input('Masukkan pesan Anda: ')
            if nama_pengguna and content:
                write_chat(f'{nama_pengguna}: {content}')
                print('Pesan berhasil dikirim!')
            else:
                print('Pesan tidak boleh kosong.')

        elif pilihan == '3':
            nama_pengguna = get_nama_pengguna()
            if not nama_pengguna:
                print('Nama pengguna tidak valid.')
                continue

            messages = read_chat()
            if not messages:
                print('\nBelum ada pesan untuk dilaporkan.')
            else:
                print('\nPesan Tersimpan:')
                for i, message in enumerate(messages, start=1):
                    print(f'{i}. {message.strip()}')
                    
                try:
                    index = int(input('\nMasukkan nomor pesan yang ingin dilaporkan: '))
                    if 1 <= index <= len(messages):
                        reported_message = messages[index - 1].strip()
                        result = report_message(reported_message, reporter=nama_pengguna)
                        if result == "already_reported":
                            print("Anda sudah melaporkan pesan ini.")
                        elif result == "success":
                            print("Pesan berhasil dilaporkan.")
                        else:
                            print(f"Error: {result}")
                    else:
                        print('Nomor pesan tidak valid.')
                except ValueError:
                    print('Input tidak valid.')

        elif pilihan == '4':
            print('Kembali ke menu utama...')
            break

        else:
            print('Pilihan tidak valid. Coba lagi.')
