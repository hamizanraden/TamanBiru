import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register():
    print("=== Registrasi Pengguna Baru ===")
    username = input("Masukkan Username: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, input("Masukkan Password: ")))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
    except sqlite3.IntegrityError:
        print("Username sudah terdaftar. Silakan coba username lain.")
    finally:
        conn.close()

def login():
    print("=== Selamat Datang di Taman Biru ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login Berhasil! Selamat datang di dashboard.")
    else:
        print("Login Gagal! Username atau password salah.")
    
    conn.close()

def main():
    create_table()  
    print("=== Aplikasi Sistem Login Mahasiswa ===")
    while True:
        choice = input("Apakah Anda sudah memiliki akun? (ya/tidak): ").strip().lower()
        if choice == 'ya':
            login()
            break
        elif choice == 'tidak':
            register()
        else:
            print("Pilihan tidak valid. Silakan pilih 'ya' atau 'tidak'.")

if __name__ == "__main__":
    main()
=======
=======


import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register():
    print("=== Registrasi Pengguna Baru ===")
    username = input("Masukkan Username: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, input("Masukkan Password: ")))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
    except sqlite3.IntegrityError:
        print("Username sudah terdaftar. Silakan coba username lain.")
    finally:
        conn.close()

def login():
    print("=== Selamat Datang di Taman Biru ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login Berhasil! Selamat datang di dashboard.")
    else:
        print("Login Gagal! Username atau password salah.")
    
    conn.close()

def main():
    create_table()  
    print("=== Aplikasi Sistem Login Mahasiswa ===")
    while True:
        choice = input("Apakah Anda sudah memiliki akun? (ya/tidak): ").strip().lower()
        if choice == 'ya':
            login()
            break
        elif choice == 'tidak':
            register()
        else:
            print("Pilihan tidak valid. Silakan pilih 'ya' atau 'tidak'.")

if __name__ == "__main__":
    main()


# Percobaan fitur login
import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register():
    print("=== Registrasi Pengguna Baru ===")
    username = input("Masukkan Username: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, input("Masukkan Password: ")))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
    except sqlite3.IntegrityError:
        print("Username sudah terdaftar. Silakan coba username lain.")
    finally:
        conn.close()

def login():
    print("=== Selamat Datang di Taman Biru ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login Berhasil! Selamat datang di dashboard.")
    else:
        print("Login Gagal! Username atau password salah.")
    
    conn.close()

def main():
    create_table()  
    print("=== Aplikasi Sistem Login Mahasiswa ===")
    while True:
        choice = input("Apakah Anda sudah memiliki akun? (ya/tidak): ").strip().lower()
        if choice == 'ya':
            login()
            break
        elif choice == 'tidak':
            register()
        else:
            print("Pilihan tidak valid. Silakan pilih 'ya' atau 'tidak'.")

if __name__ == "__main__":
    main()


