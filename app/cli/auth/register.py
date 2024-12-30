import os

def start_register(name, email, password):
    try:
        # Enkripsi sederhana untuk kata sandi (gunakan hashing pada implementasi sebenarnya)
        with open('./app/cli/data/logindatabase.txt', 'a') as file:
            file.write(f"{name},{email},{password}\n")
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def email_upi(email):
    return email.endswith('@upi.edu')

def access_register(option):
    if option == 'start_register':
        while True:
            print("Username minimal 3 karakter dan Password minimal 6 karakter.")
            name = input('Masukkan Username baru: ').strip()
            email = input('Masukkan Email (@upi.edu): ').strip()
            password = input('Masukkan Password baru: ').strip()
            
            if name and email and password:
                # Validasi panjang username dan password (bebas tergantung kelompok kita menentukannya)
                if len(name) < 3 or len(password) < 6:
                    print("Username atau Password tidak memenuhi syarat.")
                    continue
                elif not email_upi(email):
                    print("Email harus menggunakan @upi.edu")
                    continue

                try:
                    if not os.path.exists('./app/cli/data/'):
                        os.makedirs('./app/cli/data/')
                    with open('./app/cli/data/logindatabase.txt', 'r') as file:
                        existing_users = [line.strip().split(',')[0] for line in file if ',' in line]
                        if name in existing_users:
                            print("Username sudah terdaftar. Silahkan ke menu Login")
                            return
                        else:
                            start_register(name, email, password)
                            break # kembali ke menu awal 
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
