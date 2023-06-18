# for range max
for i in range(10):
    print("Hello World!")

# for range min, max
for i in range(1, 10):
    print(f"Perulangan ke- {i}")

    print(i)

# for range min, max, step
for i in range(0, 20, 2):
    print(f"step ke- {i}")

# Perulangan menurun
for i in range(20, 0, -2):
    print(i)

# fungsi break for
for i in range (1, 10):
    print("Ini Perulangan ke- ", i)
    if i == 7:
        print("Perulangan ke- ", i, "Dihentikan!")
        break

# fungsi continue for
for i in range(0, 10):
    # skip jika i == 5
    if (i ==5):
        continue

    print(i)