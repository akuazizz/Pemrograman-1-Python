#Menggunakan prosedur
def jenis_bilangan(angka):
    if angka == 0:
        print("Bilangan yang anda masukkan adalah nol")
    else:
        if angka % 2 == 0:
            print("Bilangan yang anda masukkan adalah genap")
        else:
            print("Bilangan yang anda masukkan adalah ganjil")
angka = int(input("Masukkan bilangan: "))
jenis_bilangan(angka)

#Menggunakan fungsi            
def jenis_bilangan(angka):
    if angka == 0:
        return "Merupakan angka 0"
    else:
        if angka % 2 == 0:
            return "genap"
        else:
            return "ganjil"

angka = int(input("Masukkan bilangan: "))
print("Bilangan yang anda masukkan adalah ", jenis_bilangan(angka))