import os
import re
from auth.register import email_upi

def reset_password(email):
    try:
        if not os.path.exists('./app/cli/data/logindatabase.txt'):
            print("Database belum tersedia. Silakan daftar terlebih dahulu.")
            return

        with open('./app/cli/data/logindatabase.txt', 'r') as file:
            users = [line.strip().split(',') for line in file if ',' in line]
            for user in users:
                if len(user) == 6 and user[1] == email:
                    print(f"Akun ditemukan untuk email: {email}")
                    print(f"Username: {user[0]}")
                    new_password = input("Masukkan password baru (minimal 6 karakter): ").strip()

                    if len(new_password) < 6:
                        print("Password terlalu pendek. Coba lagi.")
                        return

                    update_password(email, new_password)
                    print("Password berhasil diubah. Silakan login dengan password baru Anda.")
                    return
                if len(user) == 6 and user[1] == email:  
                    print(f"Akun ditemukan untuk email: {email}")
                    print(f"Username: {user[0]}")

                    while True:
                        new_password = input("Masukkan password baru (minimal 6 karakter, tanpa emoji): ").strip()

                        if len(new_password) < 6:
                            print("Password terlalu pendek. Coba lagi.")
                            continue

                        if not re.match(r'^[\w!@#$%^&*()]+$', new_password):
                            print("Password mengandung karakter ilegal atau emoji. Coba lagi.")
                            continue

                        update_password(email, new_password)
                        print("Password berhasil diubah. Silakan login dengan password baru Anda.")
                        return

        print("Email tidak ditemukan dalam database. Pastikan Anda telah mendaftar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def update_password(email, new_password):
    try:
        if not os.path.exists('./app/cli/data/logindatabase.txt'):
            print("Database belum tersedia.")
            return

        with open('./app/cli/data/logindatabase.txt', 'r') as file:
            users = [line.strip() for line in file if ',' in line]
        
        updated_users = []
        for user in users:
            user_data = user.split(',')
            if len(user_data) == 6 and user_data[1] == email:
                user_data[2] = new_password
            updated_users.append(','.join(user_data))

        with open('./app/cli/data/logindatabase.txt', 'w') as file:
            file.write('\n'.join(updated_users) + '\n')
    except Exception as e:
        print(f"Terjadi kesalahan saat memperbarui password: {e}")

def forgot_password():
    print("== Lupa Password ==")
    while True:
        email = input("Masukkan email yang terdaftar (@upi.edu): ").strip()
        
        if email_upi(email):
            reset_password(email)
            break
        else:
            print("Email tidak valid. Coba lagi.")
