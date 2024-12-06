import os

# Nama folder dan file untuk menyimpan riwayat chat
CHAT_FOLDER = os.path.join("app", "cli", "data")
CHAT_DATABASE = os.path.join(CHAT_FOLDER, "databasechat.txt")

def ensure_chat_folder_exists():
    """Memastikan folder untuk menyimpan file chat ada."""
    if not os.path.exists(CHAT_FOLDER):
        os.makedirs(CHAT_FOLDER)

def load_chat_history():
    """Memuat riwayat chat dari file."""
    if not os.path.exists(CHAT_DATABASE):
        return []
    with open(CHAT_DATABASE, "r", encoding="utf-8") as file:
        chats = file.readlines()
    return [chat.strip() for chat in chats]

def save_chat_to_database(sender, message):
    """Menyimpan pesan ke database chat."""
    with open(CHAT_DATABASE, "a", encoding="utf-8") as file:
        file.write(f"{sender}: {message}\n")

def display_chat_history(chats):
    """Menampilkan riwayat chat."""
    print("\n=== Riwayat Chat ===")
    for chat in chats:
        print(chat)
    print("====================\n")

