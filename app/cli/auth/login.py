# login.py

from main.main import start_lobby

def start_login(name, password):
    sukses = False
    try:
        with open('./app/data/logindatabase.txt', 'r') as file:
            for line in file:
                a, b = line.strip().split(',')  # Menggunakan strip() untuk menghapus whitespace
                if a == name and b == password:
                    sukses = True
                    break
    except FileNotFoundError:
        print("Username atau Password Anda Salah")
        return
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return
    
    if sukses:
        print('Login Berhasil')
        start_lobby()
    else:
        print('Username atau Password Anda Salah')

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

