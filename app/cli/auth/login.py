# login.py

from main.main import start_lobby

def start_login(name, password):
    while True:
        sukses = False
        try:
            with open('./app/cli/data/logindatabase.txt', 'r') as file:
                for line in file:
                    # Memisahkan semua nilai dalam baris
                    data = line.strip().split(',')
                    if len(data) >= 2:  # Pastikan ada setidaknya username dan password
                        a, b = data[0], data[1]  # Ambil username dan password
                        if a == name and b == password:
                            sukses = True
                            break
        except FileNotFoundError:
            print("Database tidak ditemukan.")
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
            name = input('Masukkan Username Anda: ')
            password = input('Masukkan Password Anda: ')
def access_login(option):
    if option == 'start_login':
        while True:
            name = input('Masukkan Username: ').strip()  # Menghapus spasi di awal dan akhir
            password = input('Masukkan Password: ').strip()  # Menghapus spasi di awal dan akhir
        
            if name and password:  # Memastikan input tidak kosong
                start_login(name, password)
                break
            else:
                print("Username dan Password tidak boleh kosong.")
    else:
        print('Opsi tidak valid.')

