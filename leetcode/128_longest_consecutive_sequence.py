
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


- check if i - 1 in set
- increment a counter to track sequence length
- At the end of each sequence, update the longest value to be max between sequence and current longest value
- restart sequence if i - 1 not in set.
- do same for next iteration
"""
import collections
class Solution:
    def __init__(self):
        pass

    def longest(self, nums):
        num_pool = set(nums)
        lngst = 0
        sequence = 0
        for num in nums:
            if (num - 1) not in num_pool:
                sequence = 0
                while (num + sequence) in num_pool:
                    sequence += 1
                lngst = max(sequence, lngst)
        return lngst



sol = Solution()
k = 2
nums = [100, 4, 200, 11, 1, 10, 3, 2, 7, 9, 8]
# t = 9

print(sol.longest(nums))
