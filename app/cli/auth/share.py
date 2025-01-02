nama_pegguna = None  # Inisialisasi variabel global

def set_nama_pengguna(name):
    global nama_pegguna
    nama_pegguna = name

def get_nama_pengguna():
    return nama_pegguna