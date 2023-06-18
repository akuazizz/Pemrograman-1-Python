nilai = int(input("Masukan bilangan bulat : "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")
elif (nilai < 0):         
    print("Bilangan", nilai, "merupakan bilangan negatif")
else:
    print("Bilangan nol")

huruf = input("Masukkan sebuah huruf : ")

vokal = ['a', 'e', 'i', 'o', 'u']
if huruf.lower() in vokal:
    print(huruf, "adalah huruf vokal.")
else:
    print(huruf, "bukan huruf vokal.") 

nilai = int(input("Masukkan nilai pembilang: "))
bagi = int(input("Masukkan nilai penyebut: "))

if bagi == 0:
    print("Error: nilai penyebut tidak boleh nol!") 
else:
    if nilai % bagi == 0:
        print("Hasil pembagian:", int(nilai / bagi))
        print("Nilai valid")
    else:
        print("Hasil pembagian:", nilai / bagi)
        print("Nilai tidak valid")

tahun = int(input("Masukkan tahun : "))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print(tahun, "adalah tahun kabisat")
        else:
            print(tahun, "bukan tahun kabisat")
    else:
        print(tahun, "adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")

