def check_code(user_code, level):
    expected_outputs = {
        1: ["Nama: Alex", "Usia: 20"],
        2: ["Total Poin: 155"],
        3: ["Item yang dikumpulkan:", "kunci", "peta", "obor", "potion", "\nHitung mundur untuk memulai petualangan:", "5", "4", "3", "2", "1", "Mulai!"]
    }
    
    user_output = exec_code(user_code)
    if user_output == expected_outputs[level]:
        return "Kamu berhasil! Semua variabel dan output benar."
    else:
        return "Coba lagi. Periksa kembali variabel dan output yang kamu buat."

def exec_code(user_code):
    # Fungsi untuk mengeksekusi kode pengguna dan mengembalikan output
    # Dalam implementasi sebenarnya, kita perlu cara yang aman untuk mengeksekusi kode
    # Misalnya menggunakan exec() dengan batasan keamanan
    namespace = {}
    exec(user_code, namespace)
    return namespace.get("output", [])
