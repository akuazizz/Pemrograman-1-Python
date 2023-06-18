def hitung_kpk(x, y):
    if x > y:
        terkecil = x
    else:
        terkecil = y
    for i in range(1, terkecil+1):
        if (x % i == 0) and (y % i == 0):
            fpb = i

    kpk = (abs(x) * abs(y)) // fpb
    return kpk

print("====PROGRAM SEDERHANA MENCARI KPK====")
x = int(input("Masukan bilangan pertama = "))
y = int(input("Masukan bilangan kedua = "))
hasil = hitung_kpk(x, y)
print("KPK = ", hasil)