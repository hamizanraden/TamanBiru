
<<<<<<< HEAD
def start_register(name, password, email, prodi, semester):
    try:
        with open('./app/cli/data/logindatabase.txt', 'a') as file:  # Ubah nama file ke logindatabase.txt
            file.write(f"{name},{password}, {email}, {prodi}, {semester}\n")
=======
import os

def start_register(name, email, password):
    try:
        # Enkripsi sederhana untuk kata sandi (gunakan hashing pada implementasi sebenarnya)
        with open('./app/cli/data/logindatabase.txt', 'a') as file:
            file.write(f"{name},{email},{password}\n")
>>>>>>> 60693f896e495a75b91f63352db4f4227aebcf29
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data")
        access_register('start_register')

def email_upi(email):
    return email.endswith('@upi.edu')

def access_register(option):
    if option == 'start_register':
        while True:
            print("Username minimal 3 karakter dan Password minimal 6 karakter.")
            name = input('Masukkan Username baru: ').strip()
            email = input('Masukkan Email (@upi.edu): ').strip()
            password = input('Masukkan Password baru: ').strip()
<<<<<<< HEAD
            email = input('Masukkan email anda: ').strip()
            prodi = input('Masukkan prodi anda: ').strip()
            semester = int(input('Masukan semester anda: '))
            if name and password:
                # Cek apakah username sudah ada
                try:
                    with open('./app/cli/data/logindatabase.txt', 'r') as file:  # Ubah nama file ke logindatabase.txt
                        existing_users = [line.split(',')[0] for line in file]
                        existing_emails = [line.split(',')[2].strip() for line in file if len(line.split(',')) > 2]
=======
            
            if name and email and password:
                # Validasi panjang username dan password(bebas tergntung kelompok kita nentuinnya)
                if len(name) < 3 or len(password) < 6:
                    print("Coba lagi.")
                    continue
                elif not email_upi(email):
                    print("Email harus menggunakan @upi.edu")
                    continue
                elif ',' in name or ',' in email or ',' in password:
                    print("Nama, email, dan password tidak boleh mengandung koma (,).")
                    continue

                try:
                    if not os.path.exists('./app/cli/data/'):
                        os.makedirs('./app/cli/data/')
                    with open('./app/cli/data/logindatabase.txt', 'r') as file:
                        existing_users = [line.strip().split(',')[0] for line in file if ',' in line]
>>>>>>> 60693f896e495a75b91f63352db4f4227aebcf29
                        if name in existing_users:
                            print("Username sudah terdaftar. Silahkan ke menu Login")
                            return
                        elif email in existing_emails:
                            print('Email sudah terdaftar, Silahkan ke menu login')
                        else:
<<<<<<< HEAD
                            start_register(name, password, email, prodi, semester)
                            access_login('start_login')
                            break
                except FileNotFoundError:
                    print("Database tidak ditemukan. Membuat database baru.")
                    start_register(name, password, email, prodi, semester)
=======
                            start_register(name, email, password)
                            break #kembali ke menu awal 
                except FileNotFoundError:
                    print("Database tidak ditemukan. Membuat database baru.")
                    start_register(name, email, password)
>>>>>>> 60693f896e495a75b91f63352db4f4227aebcf29
                    break
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")
            else:
                print("Nama, Email, dan Password tidak boleh kosong. Silakan coba lagi.")
    else:
        print('Opsi tidak valid.')
