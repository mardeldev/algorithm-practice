# Find the item in an array using binary search

def binary_search(list: list, item) -> int:
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


list = [1, 3, 5, 7, 9]
item = int(input("Please enter the item to search for: "))
print(list[binary_search(list, item)])
