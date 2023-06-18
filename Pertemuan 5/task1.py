x = int(input("Masukkan jumlah kata: "))
y = []
while len(y) + 1 <= x:
    y.append(input("Masukkan kata: "))

z = input("Masukkan kata yang ingin dicari: ")

for indeks, i in enumerate(y):
    if i == z:
        print(z, "ditemukan pada indeks ke-", indeks)
        break 
else:
    print("Indeks tidak ditemukan")