"""
Problem 1: Find the Maximum Value
Problem Statement: You're given an array of numbers. You have to find the maximum number in the array and return it.

Proposed Input: [3, 2, 9, 5, 7]

"""

class Recursive:

    def max(lst):
        if len(lst) == 1:
            return lst[0]
        max_val = lst[0]

        if max_val > max(lst[1:]):
            return max_val
        else:
            return max(lst[1:])

lst = [3, 2, 9, 5, 7]
max_r = Recursive

print(max_r.max(lst))


