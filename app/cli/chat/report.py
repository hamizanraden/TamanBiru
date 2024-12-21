import os

# Membaca data chat
def read_chat(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

# Menulis data chat
def write_chat(filename, messages):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("\n".join(messages) + "\n")

# Membaca data laporan
def read_reports(report_file):
    if not os.path.exists(report_file):
        return {}
    with open(report_file, 'r', encoding='utf-8') as file:
        reports = {}
        for line in file:
            msg_id, count = line.strip().split('|')
            reports[msg_id] = int(count)
        return reports

# Menulis data laporan
def write_reports(report_file, reports):
    with open(report_file, 'w', encoding='utf-8') as file:
        for msg_id, count in reports.items():
            file.write(f'{msg_id}|{count}\n')

# Melaporkan pesan
def report_message(chat_file, report_file, threshold=3):
    messages = read_chat(chat_file)
    reports = read_reports(report_file)

    if not messages:
        print('\nBelum ada pesan untuk dilaporkan.')
        return

    print('\nDaftar Pesan:')
    for idx, message in enumerate(messages, start=1):
        print(f'{idx}. {message.strip()}')

    try:
        msg_idx = int(input('\nMasukkan nomor pesan yang ingin dilaporkan: ')) - 1
        if 0 <= msg_idx < len(messages):
            msg_id = str(msg_idx)  # Menggunakan indeks pesan sebagai ID
            reports[msg_id] = reports.get(msg_id, 0) + 1  # Tambahkan laporan
            write_reports(report_file, reports)

            print(f"Pesan '{messages[msg_idx].strip()}' telah dilaporkan.")

            # Hapus pesan jika jumlah laporan >= threshold
            if reports[msg_id] >= threshold:
                del reports[msg_id]
                del messages[msg_idx]
                write_chat(chat_file, messages)
                write_reports(report_file, reports)
                print("Pesan telah dihapus karena terlalu banyak laporan.")
        else:
            print('Nomor pesan tidak valid.')
    except ValueError:
        print('Masukkan angka yang valid.')
