import os
def read_chat(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_chat(filename, message):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(message + '\n')

def chat_prodi(prodi, filename):
    from report.report import report_message
    
    while True:
        print(f'\n┌───────────────────୨ৎ─────────────────┐')
        print(f'│                Chat {prodi.upper()}              │')
        print('│──────────────────────────────────────│')
        print('│ 1. 📜 Lihat Pertanyaan               │')
        print('│ 2. ✍️  Ajukan Pertanyaan              │')
        print('│ 3. 💬 Balas Pertanyaan               │')
        print('│ 4. ❗ Laporkan Pesan/jawaban         │')
        print('│ 5. 🔙 Kembali                        │')
        print('└──────────────────────────────────────┘')

        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            messages = read_chat(filename)
            if not messages:
                print('\nBelum ada pertanyaan.')
            else:
                print('\nDaftar Pertanyaan:')
                for idx, message in enumerate(messages, start=1):
                    print(f'{idx}. {message.strip()}')

        elif pilihan == '2':
            from auth.login import nama_pegguna

            content = input('Masukkan pertanyaan Anda: ')
            if nama_pegguna and content:
                write_chat(filename, f'Q: {nama_pegguna}: {content}')
                print('Pertanyaan berhasil diajukan!')
            else:
                print('Nama atau pertanyaan tidak boleh kosong.')

        elif pilihan == '3':
            messages = read_chat(filename)
            if not messages:
                print('\nBelum ada pertanyaan untuk dijawab.')
            else:
                print('\nDaftar Pertanyaan:')
                for idx, message in enumerate(messages, start=1):
                    print(f'{idx}. {message.strip()}')
                try:
                    question_idx = int(input('\nPilih nomor pertanyaan untuk dijawab: ')) - 1
                    if 0 <= question_idx < len(messages):
                        reply = input('Masukkan jawaban Anda: ')
                        if reply:
                            write_chat(filename, f'A: {reply}')
                            print('Jawaban berhasil dikirim!')
                        else:
                            print('Jawaban tidak boleh kosong.')
                    else:
                        print('Nomor pertanyaan tidak valid.')
                except ValueError:
                    print('Masukkan angka yang valid.')
        elif pilihan == '4':
            from auth.login import nama_pegguna
            messages = read_chat(filename)  # filename dinamis sesuai prodi
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
                        count = report_message(reported_message, reporter=nama_pegguna, chat_file=filename)
                        print(f'Pesan berhasil dilaporkan!')
                    else:
                        print('Nomor pesan tidak valid.')
                except ValueError:
                    print('Input tidak valid.')
            
        elif pilihan == '5':
            print('Kembali ke menu utama...')
            break
        else:
            print('Pilihan tidak valid. Coba lagi.')
            
def program_studi():
    while True:
        print('\n┌───────────────────୨ৎ──────────────────┐')
        print('│         Pilih Program Studi           │')
        print('│───────────────────────────────────────│')
        print('│ 1. RPL                                │')
        print('│ 2. TEKKOM                             │')
        print('│ 3. PGSD                               │')
        print('│ 4. PMM                                │')
        print('│ 5. PGPAUD                             │')
        print('│ 6. 🔙 Kembali                         │')
        print('└───────────────────────────────────────┘')

        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            chat_prodi('RPL', 'app\cli\data\chatrpl.txt')
        elif pilihan == '2':
            chat_prodi('TEKKOM', 'app\cli\data\chattekom.txt')
        elif pilihan == '3':
            chat_prodi('PGSD', 'app\cli\data\chatpgsd.txt')
        elif pilihan == '4':
            chat_prodi('PMM', 'app\cli\data\chatpmm.txt')
        elif pilihan == '5':
            chat_prodi('PGPAUD', 'app\cli\data\chatpgpaud.txt')
        elif pilihan == '6':
            print('Kembali ke menu utama...')
            break
        else:
            print('Pilihan tidak valid. Coba lagi.')
