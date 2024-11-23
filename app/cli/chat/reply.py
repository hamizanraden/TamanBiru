# main.py

from chat.message import Chat

Chat.display_pesan()
def reply():
    pengirim = input("Masukkan nama pengirim: ")
    pesan = input("Masukkan pesan: ")
    chat = Chat(pengirim, pesan)

    while True:
        add_more = input("Apakah ingin menambahkan balasan? (y/n): ").strip().lower()
        if add_more == 'y':
            reply_pengirim = input("Masukkan nama pengirim balasan: ")
            reply_pesan = input("Masukkan pesan balasan: ")
            chat.add_reply(reply_pengirim, reply_pesan)
        else:
            break

    print("\nPercakapan:")
    chat.display_pesan()


