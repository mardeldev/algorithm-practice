def sum(lst: int | list) -> int:
    if not lst:
        return 0
    first_item = lst[0]

    if isinstance(first_item, list):
        return sum(first_item) + sum(lst[1:])
    else:
        return first_item + sum(lst[1:])


lst = [[2, 6], 4, 6]
print(sum(lst))
