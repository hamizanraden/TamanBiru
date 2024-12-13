# login.py

from main.main import start_lobby

def start_login(name, password):
    while True:
        sukses = False
        try:
            with open('./app/cli/data/logindatabase.txt', 'r') as file:
                for line in file:
                    # Pastikan baris memiliki format yang benar
                    data = line.strip().split(',')
                    if len(data) != 2:  # Abaikan baris yang tidak sesuai format
                        continue
                    
                    a, b = data
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
            print('Username atau Password Anda Salah. Coba lagi.')
            name = input('Masukkan Username Anda: ').strip()
            password = input('Masukkan Password Anda: ').strip()

def access_login(option):
    if option == 'start_login':
        while True:
            name = input('Masukkan Username: ').strip()
            password = input('Masukkan Password: ').strip()
        
            if name and password:
                start_login(name, password)
                break
            else:
                print("Username dan Password tidak boleh kosong.")
    else:
        print('Opsi tidak valid.')