import os
def read_chat():
    if not os.path.exists('./app/cli/data/chatAll.txt'):
        return []
    with open('./app/cli/data/chatAll.txt', 'r', encoding='utf-8') as file:
        return file.readlines()
    
def write_chat(message):
    with open('./app/cli/data/chatAll.txt', 'a', encoding='utf-8') as file:
        file.write(message + '\n')

def read_chat():
    if not os.path.exists('./app/cli/data/reports_all.txt'):
        return []
    with open('./app/cli/data/reports_all.txt', 'r', encoding='utf-8') as file:
        return file.readlines()

def chat_all():
    chat_file = './app/cli/data/chatAll.txt'
    report_file = './app/cli/data/reports_all.txt'
    
    
    while True:
        print('\n┌───────────────────୨ৎ──────────────────┐')
        print('│               Chat All                │')
        print('│───────────────────────────────────────│')
        print('│ 1. 📜 Lihat Pesan                     │')
        print('│ 2. ✍️  Kirim Pesan                     │')
        print('│ 3. 🔙 Kembali                         │')
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
            username = input('\nMasukkan nama Anda: ')
            content = input('Masukkan pesan Anda: ')
            if username and content:
                write_chat(f'{username}: {content}')
                print('Pesan berhasil dikirim!')
            else:
                print('Nama atau pesan tidak boleh kosong.')

        elif pilihan == '3':
            print('Kembali ke menu utama...')
            break

        else:
            print('Pilihan tidak valid. Coba lagi.')