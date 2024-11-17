from chat.message import message

def reply_message(reply):
    if reply :
        message.append(reply)
        print("Message replied")
    else:
        print("No message to reply")

def display_reply():
    if message:
        for i, reply in enumerate(message, 1):
            print (f"Reply {i}: {reply}")
    else:
        print("No messages to display")

while True:
    print ("\n 1. Lihat Komentar")
    print ("2. Tambahkan komentar")
    print ("3. Keluar")

    memilih= input ("Masukan pilihan: ")

    if memilih == "1":
        user_reply = input("Masukan komentar: ")
        reply_message(user_reply)
    elif memilih == "2":
        display_reply()
    elif memilih == "3":
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    else:
        print("Pilihan tidak tersedia")