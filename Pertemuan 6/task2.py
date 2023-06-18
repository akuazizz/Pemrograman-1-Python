#Menggunakan prosedur
def hitung_keliling_luas_lingkaran(jari):
    keliling = 2 * 3.14 * jari
    luas = 3.14 * jari * jari
    print("Keliling Lingkaran : ", keliling)
    print("Luas lingkaran : ", luas)

jari = int(input("Masukkan jari-jari : "))
hitung_keliling_luas_lingkaran(jari)

#Menggunakan function
def hitung_keliling_lingkaran(jari):
    return 2 * 3.14 * jari

def hitung_luas_lingkaran(jari):
    return 3.14  * jari * jari

jari = int(input("Masukkan jari-jari : "))
print("Keliling Lingkaran : ", hitung_keliling_lingkaran(jari))
print("Luas Lingkaran : ", hitung_luas_lingkaran(jari))