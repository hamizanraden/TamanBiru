from main.main import start_lobby
from auth.register import access_register

def start_login(name, password):
    batas = 0  
    Kesempatan_login = 3  

    while batas < Kesempatan_login:
        sukses = False
        try:
            with open('./app/cli/data/logindatabase.txt', 'r') as file:
                for line in file:
                    # Pastikan baris memiliki format yang benar
                    data = line.strip().split(',')
                    if len(data) != 3:  # Abaikan baris yang tidak sesuai format
                        continue
                    
                    a, _, b = data  # Ambil kolom name dan password, abaikan email
                    if a == name and b == password:
                        sukses = True
                        break
        except FileNotFoundError:
            print("Database tidak ditemukan. Silakan registrasi terlebih dahulu.")
            return 
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            return
        
        if sukses:
            print('Login Berhasil')
            start_lobby()
            break
        else:
            batas += 1 
            print(f"Username atau Password Anda Salah. Kesempatan Anda {Kesempatan_login - batas}x kali lagi!")
            if batas < Kesempatan_login:
                name = input("Masukkan Username Anda: ").strip()
                password = input("Masukkan Password Anda: ").strip()
            else:
                from run import display_main_menu
                print("Tekan Enter untuk kembali ke halaman login")
                input()
                display_main_menu()

def access_login(option):
    if option == 'start_login':
        while True:
            name = input("Masukkan Username: ").strip()
            password = input("Masukkan Password: ").strip()
        
            if name and password:
                start_login(name, password)
                break
            else:
                print("Username dan Password tidak boleh kosong.")
    else:
        print("Opsi tidak valid.")
