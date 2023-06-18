# Validasi nilai

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