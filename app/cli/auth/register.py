import re
from auth.login import access_login

def is_valid_username(username):
    # Validasi hanya untuk karakter alfanumerik dan simbol tertentu (._-)
    return bool(re.search(r'^[A-Za-z0-9._-]+$', username))

def is_valid_password(password):
    # Validasi untuk memastikan password tidak mengandung karakter yang tidak diinginkan
    return bool(re.search(r'^[A-Za-z0-9!@#$%^&*()_+=.-]+$', password))

def start_register(name, password):
    try:
        with open('./app/cli/data/logindatabase.txt', 'a') as file:
            file.write(f"{name},{password}\n")
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def access_register(option):
    if option == 'start_register':
        while True:
            name = input('Masukkan Username baru: ').strip()
            password = input('Masukkan Password baru: ').strip()

            if not name or not password:
                print("Username dan Password tidak boleh kosong. Silakan coba lagi.")
                continue

            if not is_valid_username(name):
                print("Username hanya boleh mengandung huruf, angka, dan simbol ._-.")
                continue

            if not is_valid_password(password):
                print("Password mengandung karakter yang tidak diizinkan.")
                continue

            try:
                # Cek apakah username sudah ada di database
                with open('./app/cli/data/logindatabase.txt', 'r') as file:
                    existing_users = []
                    for line in file:
                        try:
                            user, passw = line.strip().split(',', 1)
                            existing_users.append(user)
                        except ValueError:
                            print(f"Peringatan: Format baris tidak valid di database: {line.strip()}")
                            continue

                    if name in existing_users:
                        print("Username sudah terdaftar. Silakan ke menu Login.")
                        return

                # Jika username belum ada, lakukan registrasi
                start_register(name, password)
                access_login('start_login')
                break

            except FileNotFoundError:
                print("Database tidak ditemukan. Membuat database baru.")
                start_register(name, password)
                break

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
    else:
        print('Opsi tidak valid.')
