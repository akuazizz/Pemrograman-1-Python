print("~~~~~MENCARI BILANGAN GENAP~~~~~")
range_max = int(input("Masukkan bilangan maksimal: "))
for i in range(1, range_max):
    if i % 2 == 0:
        print(i)