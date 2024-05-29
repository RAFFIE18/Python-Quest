from levels import level1, level2, level3
from utils.feedback import check_code

def main():
    print("Selamat datang di Python Quest!")
    
    # Menjalankan Level 1
    print("\n=== Level 1: Variabel Dasar ===")
    user_code = level1.run()
    feedback = check_code(user_code, level=1)
    print(feedback)
    
    # Menjalankan Level 2
    print("\n=== Level 2: Operasi Aritmatika ===")
    user_code = level2.run()
    feedback = check_code(user_code, level=2)
    print(feedback)
    
    # Menjalankan Level 3
    print("\n=== Level 3: Pengulangan dengan Loop ===")
    user_code = level3.run()
    feedback = check_code(user_code, level=3)
    print(feedback)
    
if __name__ == "__main__":
    main()
