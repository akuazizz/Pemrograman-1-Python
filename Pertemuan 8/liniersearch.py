def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword '{keyword}' found at index {i}")
            return i
    print(f"Keyword '{keyword}' not found")
    return -1

data = [23, 53, 43, 78, 90, 10, 32]
keyword = input("Input keyword: ")
linear_search(keyword, data)