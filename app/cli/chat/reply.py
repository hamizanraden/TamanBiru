from chat.message import save_chat_to_database

def reply_to_message(sender, message):
    save_chat_to_database(sender, f"[REPLY] {message}")
    print(f"{sender} membalas: {message}")

# Contoh penggunaan
if __name__ == "__main__":
    sender = input("Masukkan nama Anda: ")
    message = input("Masukkan pesan balasan Anda: ")
    reply_to_message(sender, message)
