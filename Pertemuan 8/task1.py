def linear_search(search_input, database):
    for i in range(len(database)):
        if str(database[i][0]).lower() == search_input.lower():
            print(f"Plat dengan nomer '{search_input}' ada pada database dengan index {i}")
            return i
    print(f"Plat dengan nomer '{search_input}' tidak ada pada database")
    return -1

database = [["R 2477 SR"], ["R 1234 DJ"], ["R 7015 LP"], ["R 0201 RR"], 
            ["R 3304 DA"], ["R 2401 SK"], ["R 2103 RT"], ["R 1708 RI"], 
            ["R 1111 SR"], ["R 4987 LH"]]
search_input = input("Masukkan plat yang ingin dicari : ")
linear_search(search_input, database)