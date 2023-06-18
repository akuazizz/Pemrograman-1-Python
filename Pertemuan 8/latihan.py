#Binary Search
def bubble_sort(data, keyword):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return binary_search(keyword, data)

def binary_search(keyword, data):
    sorted_data = data
    print(f'Data (sorted) = {sorted_data}')
    left = 0
    right = len(sorted_data) - 1
    while left <= right:
        mid = (left + right) // 2
        str_data = str(sorted_data[mid]).lower()
        if str_data > keyword.lower():
            right = mid - 1
        elif str_data < keyword.lower():
            left = mid + 1
        else:
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid
    print(f"Keyword {keyword} has not been found")
    return -1

data = [23, 45, 4, 78, 10, 9]
keyword = input("Input keyword: ")
bubble_sort(data, keyword)

# Linear Search
def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword '{keyword}' has been found at index {i}")
            return i
    print(f"Keyword '{keyword}' has not been found")
    return -1

data = [23, 3, 4, 10, 32]
keyword = input("Input Keyword: ")
linear_search(keyword, data)