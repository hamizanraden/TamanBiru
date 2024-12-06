from chat.message import *

def main():
    print("Selamat datang di Grup Chat!")
    print("Ketik 'keluar' untuk mengakhiri program.")

    ensure_chat_folder_exists()
    chat_history = load_chat_history()
    display_chat_history(chat_history)

    while True:
        sender = input("Masukkan nama Anda: ").strip()
        if not sender:
            print("Nama tidak boleh kosong.")
            continue

        message = input("Masukkan pesan Anda: ").strip()
        if message.lower() == "keluar":
            print("Keluar dari grup chat. Sampai jumpa!")
            break

        if message:
            save_chat_to_database(sender, message)
            print(f"{sender}: {message}")

if __name__ == "__main__":
    main()