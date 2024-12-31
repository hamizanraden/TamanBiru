import os

def settings_menu():
    while True: 
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│               Settings                │')
        print('│───────────────────────────────────────│')
        print('│ 1. 🌑 Dark Mode                       │')
        print('│ 2. 🧾 Profile                         │')
        print('│ 3. 🔑 Change Password                 │')
        print('│ 4. 🌐 Language                        │')
        print('│ 5. 🔙 Kembali                         │')
        print('└───────────────────────────────────────┘')
    
    # User input
        choice = input("Pilih menu: ")

    # Kondisional untuk memilih menu
        if choice == "1":
            print("Dark Mode aktif")
        elif choice == "2":
            print("Profile")
        elif choice == "3":
            print("Change Password")
        elif choice == "4":
            print("Language")
        elif choice == "5":
            print("Kembali ke Main Menu")
            break
        else:
            print("Pilihan tidak valid")