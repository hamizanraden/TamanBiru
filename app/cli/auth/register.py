from auth.login import access_login

def start_register(name, password):
    try:
        with open('./app/cli/data/logindatabase.txt', 'a') as file:  # Ubah nama file ke logindatabase.txt
            file.write(f"{name},{password}\n")
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def access_register(option):
    if option == 'start_register':
        while True:
            name = input('Masukkan Username baru: ').strip()
            password = input('Masukkan Password baru: ').strip()
            
            if name and password:
                # Cek apakah username sudah ada
                try:
                    with open('./app/cli/data/logindatabase.txt', 'r') as file:  # Ubah nama file ke logindatabase.txt
                        existing_users = [line.split(',')[0] for line in file]
                        if name in existing_users:
                            print("Username sudah terdaftar. Silahkan ke menu Login")
                            return
                        else:
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
                print("Username dan Password tidak boleh kosong. Silakan coba lagi.")
    else:
        print('Opsi tidak valid.')