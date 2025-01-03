import os
import re

def start_register(name, email, password, prodi, semester, notelp):
    try:
        # Enkripsi sederhana untuk kata sandi (gunakan hashing pada implementasi sebenarnya)
        with open('./app/cli/data/logindatabase.txt', 'a') as file:
            file.write(f"{name},{email},{password},{prodi},{semester},{notelp}\n")
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def email_upi(email):
    return email.endswith('@upi.edu')

def access_register(option):
    if option == 'start_register':
        if not os.path.exists('./app/cli/data/'):
            os.makedirs('./app/cli/data/', exist_ok=True)
        
        while True:
            # Validasi Username
            while True:
                name = input('Masukkan Username baru (min 3 karakter dan maks 20 karakter): ').strip()
                if len(name) < 3:
                    print("Username harus minimal 3 karakter. Coba lagi.")
                elif len(name) > 20:
                    print("Username maksimal 20 karakter. Coba lagi.")
                elif not name.isalpha():
                    print("Username hanya boleh berisi huruf. Coba lagi.")
                elif ',' in name:
                    print("Username tidak boleh mengandung koma (,). Coba lagi.")
                else:
                    break

            # Validasi Email
            while True:
                email = input('Masukkan Email (@upi.edu): ').strip()
                if not email_upi(email):
                    print("Email harus menggunakan @upi.edu. Coba lagi.")
                elif ',' in email:
                    print("Email tidak boleh mengandung koma (,). Coba lagi.")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    print("Email mengandung karakter ilegal atau emoji. Coba lagi.")
                else:
                    break

            # Validasi Password
            while True:
                password = input('Masukkan Password baru (min 6 karakter): ').strip()
                if len(password) < 6:
                    print("Password harus minimal 6 karakter. Coba lagi.")
                elif not password.isalnum():
                    print("Password harus alfanumerik. Coba lagi.")
                elif ',' in password:
                    print("Password tidak boleh mengandung koma (,). Coba lagi.")
                else:
                    break

            # Validasi Prodi
            while True:
                prodi = input('Masukkan prodi (RPL, TEKKOM, PMM, PGSD, PGPAUD): ').strip().upper()
                if prodi not in ("RPL", "TEKKOM", "PMM", "PGSD", "PGPAUD"):
                    print("Masukkan prodi yang benar. Coba lagi.")
                elif ',' in prodi:
                    print("Prodi tidak boleh mengandung koma (,). Coba lagi.")
                else:
                    break

            # Validasi Semester
            while True:
                semester = input('Masukkan semester: ').strip()
                if not semester.isdigit():
                    print("Semester harus berupa angka. Coba lagi.")
                elif not (1 <= int(semester) <= 14):
                    print("Semester tidak valid. Coba lagi.")
                else:
                    break

            # Validasi Nomor Telepon
            while True:
                notelp = input('Masukkan nomor telefon: ').strip()
                if not notelp.isdigit():
                    print("Nomor telefon harus berupa angka. Coba lagi.")
                elif len(notelp) < 10:
                    print("Nomor telefon harus minimal 10 digit. Coba lagi.")
                elif ',' in notelp:
                    print("Nomor telefon tidak boleh mengandung koma (,). Coba lagi.")
                else:
                    break

            # Cek Username Unik
            try:
                with open('./app/cli/data/logindatabase.txt', 'r') as file:
                    existing_users = [line.strip().split(',')[0] for line in file if ',' in line]
                    if name in existing_users:
                        print("Username sudah terdaftar. Silahkan ke menu Login.")
                        return
            except FileNotFoundError:
                print("Database tidak ditemukan. Membuat database baru.")

            # Registrasi Data
            start_register(name, email, password, prodi, semester, notelp)
            break
    else:
        print('Opsi tidak valid.')
