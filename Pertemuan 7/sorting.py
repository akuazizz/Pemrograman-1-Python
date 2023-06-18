# import timeit

# print("Ascending")
# print(" ")

# insertion sort
def insertion_sort(array):
  start = timeit.default_timer()
  for i in range(1, len(array)):
    item = array [i]
    j = i - 1

    while j >= 0 and array[j] > item:
      array[j + 1] = array[j]
      j -= 1
    
      array[j + 1] = item

  stop = timeit.default_timer()
  print(f"insertion sort succesfull elapsed time : + {stop - start}")
  return array

# bubble sorting
def bubble_sort(array):
  for i in range(len(array)):
    for j in range(len(array)-i-1):
      if array[j] < array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]

  return array
array2 = [12, 19, 20, 22, 11, 28, 33]
bubble_sort(array2)
print(array2)

# selection sort
def selection_sort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
      if array[min_index] < array [j] :
        min_index = j
        array[i], array[min_index] = array[min_index], array[i]

  return array
array2 = [12, 19, 20, 22, 11, 28, 33]
selection_sort(array2)
print(array2)


list_1 = [2, 4, 1, 45, 33, 65, 6, 8]
print(f"Before: {list_1}")

selection_sort(list_1)
print(f"After: {list_1}")




def insertion_sort(array):
  for i in range(1, len(array)):
    item = array [i]
    j = i - 1

    while j >= 0 and array[j] < item:
      array[j + 1] = array[j]
      j -= 1
    
      array[j + 1] = item

  return array
test = [15, 20, 12, 13, 17, 11]
insertion_sort(test)
print(test)