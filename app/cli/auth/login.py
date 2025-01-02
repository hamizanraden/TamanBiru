from main.main import start_lobby
from auth.register import access_register
from auth.forgot import forgot_password
from auth.share import set_nama_pengguna

def start_login(name, password):
    batas = 3  
    while batas > 0:
        sukses = False
        try:
            with open('./app/cli/data/logindatabase.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) != 6:
                        continue
                    a, _, b, _, _, _ = data
                    if a == name and b == password:
                        sukses = True
                        set_nama_pengguna(name)
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
            batas -= 1
            if batas > 0:
                print(f"Username atau Password Anda salah. Kesempatan Anda {batas}x lagi!")
            else:
                print("Kesempatan login Anda telah habis.")
                from run import display_main_menu
                print("Tekan Enter untuk kembali ke halaman login.")
                input()
                display_main_menu()
                return

            while True:
                print("┌───────────────────୨ৎ──────────────────┐")
                print("│  1. Coba Lagi     │ 2. Lupa Password  │")
                print("└───────────────────୨ৎ──────────────────┘")

                lupa = input('Pilih opsi: ')

                if lupa == '1':
                    if batas >= 1:
                        name = input("Masukkan Username Anda: ").strip()
                        password = input("Masukkan Password Anda: ").strip()
                        break
                elif lupa == '2':
                    forgot_password()
                    return
                else:
                    print("Pilihan tidak tersedia. Silakan pilih opsi yang tersedia.")
                    continue


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
