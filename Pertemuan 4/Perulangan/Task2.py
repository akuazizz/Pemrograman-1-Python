print("====Program Sederhana Menghitung Pangkat====")
bil = int (input("Masukan bilangan = "))
pangkat = int (input("Masukan pencacah = "))
hasil = bil

for i in range (pangkat -1):
    hasil *= bil
    
print("Hasil pangkat = ", hasil)