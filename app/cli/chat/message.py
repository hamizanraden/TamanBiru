import sqlite3

conn = sqlite3.connect('chat_questions.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    question TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    answer TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions (id)
)
''')
conn.commit()

def pilih_kolom_chat():
    while True:
        print("Pilih kolom chat:")
        print("1. Semua")
        print("2. Jurusan")
        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan in ['1', '2']:
            return 'Semua' if pilihan == '1' else 'Jurusan'
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tulis_pertanyaan():
    return input("Tulis pertanyaan Anda: ")

def kirim_pertanyaan(kategori, pertanyaan):
    try:
        cursor.execute('INSERT INTO questions (category, question) VALUES (?, ?)', (kategori, pertanyaan))
        conn.commit()
        return True
    except Exception as e:
        print(f"Terjadi kesalahan saat mengirim pertanyaan: {e}")
        return False

def tampilkan_pertanyaan_dan_jawaban():
    cursor.execute('''
    SELECT questions.id, questions.category, questions.question, answers.answer 
    FROM questions 
    LEFT JOIN answers ON questions.id = answers.question_id
    ''')
    rows = cursor.fetchall()
    print("\nPertanyaan dan Jawaban:")
    for row in rows:
        if row[3]: 
            print(f"[{row[0]}] [{row[1]}] Pertanyaan: {row[2]} - Jawaban: {row[3]}")
        else:
            print(f"[{row[0]}] [{row[1]}] Pertanyaan: {row[2]} - Belum ada jawaban.")

def jawab_pertanyaan():
    tampilkan_pertanyaan_dan_jawaban()
    question_id = input("Masukkan ID pertanyaan yang ingin Anda jawab: ")
    answer = input("Tulis jawaban Anda: ")
    try:
        cursor.execute('INSERT INTO answers (question_id, answer) VALUES (?, ?)', (question_id, answer))
        conn.commit()
        print("Jawaban berhasil dikirim!")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengirim jawaban: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Ajukan Pertanyaan")
        print("2. Jawab Pertanyaan")
        print("3. Lihat Pertanyaan dan Jawaban")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            kategori = pilih_kolom_chat()
            pertanyaan = tulis_pertanyaan()
            if kirim_pertanyaan(kategori, pertanyaan):
                print("Pertanyaan berhasil dikirim!")
            else:
                print("Pertanyaan gagal dikirim.")
        elif pilihan == '2':
            jawab_pertanyaan()
        elif pilihan == '3':
            tampilkan_pertanyaan_dan_jawaban()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

conn.close()