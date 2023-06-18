print("~~~~~SISTEM LOGIN SEDERHANA~~~~~")
username = "username"
password = "password123"
max_attempts = 3
attempts = 0

while True:
    user_input = input("Masukkan username: ")
    user_input = input("Masukkan password: ")
    if user_input == password:
        print("Password benar. Anda berhasil login!")
        break
    else:
        attempts += 1
        if attempts >= max_attempts:
            print("Anda telah mencoba login sebanyak 3 kali. Coba lagi nanti.")
            break
        else:
            print("Coba cek kembali, username atau password salah")

