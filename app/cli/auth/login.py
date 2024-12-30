from main.main import start_lobby
from auth.register import access_register
from auth.forgot import forgot_password

def start_login(name, password):
    batas = 3  
      

    while batas > 0:
        sukses = False
        try:
            with open('./app/cli/data/logindatabase.txt', 'r') as file:
                for line in file:
<<<<<<< HEAD
                    # Memisahkan semua nilai dalam baris
                    data = line.strip().split(',')
                    if len(data) >= 2:  # Pastikan ada setidaknya username dan password
                        a, b = data[0], data[1]  # Ambil username dan password
                        if a == name and b == password:
                            sukses = True
                            break
        except FileNotFoundError:
            print("Database tidak ditemukan.")
=======
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
>>>>>>> 60693f896e495a75b91f63352db4f4227aebcf29
            return 
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            return
        
        if sukses:
            print('Login Berhasil')
            start_lobby()
            break
        else:
<<<<<<< HEAD
            print('Username atau Password Anda Salah. Coba lagi.')
            name = input('Masukkan Username Anda: ')
            password = input('Masukkan Password Anda: ')
=======
            batas -= 1
            if batas > 0:
                print(f"Username atau Password Anda Salah. Kesempatan Anda {batas}x kali lagi!")
            
            else:
                print("Kesempatan login Anda telah habis.")
                from run import display_main_menu
                print("Tekan Enter untuk kembali ke halaman login")
                input()
                display_main_menu()
                return  # Keluar dari fungsi
            
            while True:
                print("┌───────────────────୨ৎ──────────────────┐")
                print("│  1. Coba Lagi     │ 2. Lupa Password  │")
                print("└───────────────────୨ৎ──────────────────┘")

                lupa = input('Pilih opsi: ')

                if lupa == '1':
                    if batas >=1:
                        name = input("Masukkan Username Anda: ").strip()
                        password = input("Masukkan Password Anda: ").strip()
                        break
                elif lupa == '2':
                    forgot_password()
                    return
                else:
                    print("Pilihan tidak tersedia. Silakan pilih opsi yang tersedia.")
                    continue
>>>>>>> 60693f896e495a75b91f63352db4f4227aebcf29
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
