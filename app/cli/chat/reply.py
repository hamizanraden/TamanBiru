from chat.message import Chat

def reply():
    sender = input("Nama pengirim: ")
    message = input("Masukkan pesan/balasan: ")
    chat = chat(sender, message)

    while True:
        add_more = input("Apakah ingin menambahkan balasan? (y/n): ").strip().lower()
        if add_more == 'y':
            reply_pengirim = input("Nama pengirim: ")
            reply_pesan = input("Masukkan pesan: ")
            chat.add_reply(reply_pengirim, reply_pesan) 
        else:
            break