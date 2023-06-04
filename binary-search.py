# Find the item in an array using binary search

def binary_search(list: list, item) -> int:
    # set low index to zero
    low = 0
    # set high index to last item index
    high = len(list) - 1
    while low <= high:  # <-- execute while we are not on the last item of search
        mid = (low + high) // 2  # <-- set the mid point of array
        # <-- the current guess is the middle item in the array
        guess = list[mid]
        if guess == item:  # <-- if the current guess equals the search item then return the array index
            return mid
        # if the current place in the search is higher than the search item then set the high index to be the mid index (this halves the list towards the lower end)
        if guess > item:
            high = mid - 1
        # else the current spot must be lower, so set the low index to be mid (this halves the list towards the higher end)
        else:
            low = mid + 1
    return None


list = [1, 3, 5, 7, 9]
item = int(input("Please enter the item to search for: "))
print(list[binary_search(list, item)])

# Things to do: Catch exception for when the item is the wrong data type. Same for return of 'None'
