from auth.login import access_login
import re

def start_register(name, email, password):
    try:
        with open('./app/cli/data/logindatabase.txt', 'a') as file:
            file.write(f"{name},{email},{password}\n")
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def access_register(option):
    if option == 'start_register':
        while True:
            name = input('Masukkan Nama baru: ').strip()
            email = input('Masukkan Email baru (harus domain @email.edu): ').strip()
            password = input('Masukkan Password baru: ').strip()

            if name and email and password:
                # Validasi email dengan domain @email.edu
                if not re.match(r'^\S+@email\.edu$', email):
                    print("Email harus menggunakan domain @email.edu. Silakan coba lagi.")
                    continue

                # Cek apakah email sudah terdaftar
                try:
                    with open('./app/cli/data/logindatabase.txt', 'r') as file:
                        existing_users = [line.strip().split(',') for line in file if line.strip()]
                        if any(user[1] == email for user in existing_users):
                            print("Email sudah terdaftar. Silakan ke menu Login.")
                            access_login('start_login')
                            return
                        else:
                            start_register(name, email, password)
                            access_login('start_login')
                            break
                except FileNotFoundError:
                    print("Database tidak ditemukan. Membuat database baru.")
                    start_register(name, email, password)
                    break
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")
            else:
                print("Nama, Email, dan Password tidak boleh kosong. Silakan coba lagi.")
    else:
        print('Opsi tidak valid.')
