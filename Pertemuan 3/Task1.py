# Huruf vokal dan konsonan

huruf = input("Masukkan sebuah huruf : ")

vokal = ['a', 'e', 'i', 'o', 'u']
if huruf.lower() in vokal:
    print(huruf, "adalah huruf vokal.")
else:
    print(huruf, "bukan huruf vokal.") 