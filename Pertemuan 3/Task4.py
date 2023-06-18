# menghitung biaya operasi

data = {
    'penyakit': {'katarak': '7.500.000', 'plusminus': '5.000.000', 'silinder': '4.000.000',
                 'jantungkoroner': '500.000.000', 'katupjantung': '350.000.000', 'ototjantung': '450.000.000'}

}

for key, value in data.items():
    print("===== MENU HITUNG BIAYA OPERASI =====")
    print("1.Hitung Biaya Operasi Mata\n2.Hitung Biaya Operasi Jantung")
    p = int(input("Masukkan pilihan : "))

    if (p == 1):
        print("JENIS PENYAKIT MATA\n1.Katarak\n2.Plus/Minus\n3.Silinder")
        pp = int(input("Masukkan jenis penyakit mata : "))
        if (pp == 1):
            print("Biaya Operasi Mata Katarak : ", value['katarak'])
        elif (pp == 2):
            print("Biaya Operasi Mata Plus/Minus : ", value['plusminus'])
        elif (pp == 3):
            print("Biaya Operasi Mata Silinder : ", value['silinder'])
    elif (p == 2):
        print("JENIS PENYAKIT JANTUNG\n1.Jantung Koroner\n2.Katup Jantung\n3.Otot Jantung")
        pp2 = int(input("Masukkan jenis penyakit jantung : "))
        if (pp2 == 1):
            print("Biaya Operasi Jantung Koroner : ", value['jantungkoroner'])
        elif (pp2 == 2):
            print("Biaya Operasi Katup Jantung : ", value['katupjantung'])
        elif (pp2 == 3):
            print("Biaya Operasi Otot Jantung : ", value['ototjantung'])
    else:
        print("Tidak ada dalam pilihan")

