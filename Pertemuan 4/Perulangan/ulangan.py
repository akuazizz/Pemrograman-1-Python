bilangan = int(input("Masukkan bilangan bulat positif antara 1 hingga 100: "))

if bilangan >= 1 and bilangan <= 100:
    if bilangan % 6 == 0:
        print(f"{bilangan} adalah kelipatan 6.")
    else:
        print(f"{bilangan} bukan kelipatan 6.")
else:
    print("Bilangan yang dimasukkan tidak valid. Pastikan bilangan berada dalam rentang 1 hingga 100.")