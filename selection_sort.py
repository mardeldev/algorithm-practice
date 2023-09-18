def findSmallestNumber(arr):
    smallest_index = 0
    smallest_num = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    sorted_list = []
    for i in range(len(arr)):
        smallest_index = findSmallestNumber(arr)
        sorted_list.append(arr.pop(smallest_index))
    return sorted_list


arr = [5, 3, 6, 2, 10]
print(selectionSort(arr))