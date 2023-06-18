# menggunakan function
def hitung_keliling_persegi(sisi):
    return 4 * sisi 

def hitung_luas_persegi(sisi):
    return sisi * sisi

sisi = int(input("Masukkan sisi persegi: "))

print("Keliling persegi: ", hitung_keliling_persegi(sisi))
print("Luas persegi: ", hitung_luas_persegi(sisi))

# menggunakan prosedur
def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    print("Keliling persegi: ", keliling)
    luas = sisi * sisi
    print("Luas persegi: ", luas)

sisi = int(input("Masukkan sisi persegi: "))
keliling_luas_persegi(sisi)