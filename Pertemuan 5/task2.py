x = int(input("Masukkan jumlah mata kuliah: "))
y = []
urutan = 1
while len(y) + 1 <= x:
    y.append(float(input(f"Masukkan nilai mata kuliah ke- {urutan} : ")))
    urutan += 1

total_nilai = sum(y)
rata_nilai = total_nilai/x
urutan_nilai = 1

if rata_nilai >= 90 and rata_nilai < 100:
    print("Hasil Predikat A dengan nilai : ")
    for i in y:
        print(f"Mata kuliah ke-{urutan_nilai} : {i}")
        urutan_nilai += 1
elif rata_nilai >= 70 and rata_nilai < 90:
    print("Hasil Predikat B dengan nilai : ")
    for i in y:
        print(f"Mata kuliah ke-{urutan_nilai} : {i}")
        urutan_nilai += 1
elif rata_nilai >= 50 and rata_nilai < 70:
    print("Hasil Predikat C dengan nilai : ")
    for i in y:
        print(f"Mata kuliah ke-{urutan_nilai} : {i}")
        urutan_nilai += 1
elif rata_nilai >= 30 and rata_nilai < 50:
    print("Hasil Predikat D dengan nilai : ")
    for i in y:
        print(f"Mata kuliah ke-{urutan_nilai} : {i}")
        urutan_nilai += 1
elif rata_nilai >= 0 and rata_nilai < 30:
    print("Hasil Predikat E dengan nilai : ")
    for i in y:
        print(f"Mata kuliah ke-{urutan_nilai} : {i}")
        urutan_nilai += 1
else:
    print("Nilai tidak valid")