"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:
    def topKFrequent(nums, k) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # A list to hold the freq: [0][1][2][3][4][5][6]
        #                          [ ][3][2][1][ ][ ][ ]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for val in count:
            freq[count[val]].append(val)

        result = []
        iterator = 0
        for sublist in reversed(freq):
            if len(sublist) > 0 and iterator < k:
                for num in sublist:
                    result.append(num)
                    iterator += 1
        return result


s1 = Solution
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(s1.topKFrequent(nums, k))