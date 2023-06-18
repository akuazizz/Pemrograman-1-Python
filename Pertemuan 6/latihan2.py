bil1 = int(input("Masukkan bilangan 1: "))
bil2 = int(input("Masukkan bilangan 2: "))

def hitung_bilangan_lebih_besar(bil1, bil2):
    if bil1 > bil2:
        print("Bilangan yang lebih besar adalah ", bil1)
    elif bil1 == bil2:    
        print("Tidak ada bilangan yang lebih besar.")
    else:
        print("Bilangan yang lebih besar adalah ", bil2)

hitung_bilangan_lebih_besar(bil1, bil2)