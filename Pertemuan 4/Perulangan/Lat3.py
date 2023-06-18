print("~~~~~PROGRAM MENCARI FPB~~~~~")
# meminta user untuk memasukkan dua bilangan bulat
num1 = int(input("Masukkan bilangan bulat pertama: "))
num2 = int(input("Masukkan bilangan bulat kedua: "))

# mencari bilangan terkecil dari kedua bilangan yang diinputkan
min_num = min(num1, num2)

# inisialisasi variabel fpb dengan nilai awal 1
fpb = 1

# loop dari 1 hingga bilangan terkecil yang diinputkan
for i in range(1, min_num + 1):
    # jika i merupakan faktor dari kedua bilangan, maka update nilai fpb
    if num1 % i == 0 and num2 % i == 0:
        fpb = i

# cetak nilai fpb
print("FPB dari", num1, "dan", num2, "adalah", fpb)