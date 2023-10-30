class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        # prefix:
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre = res[i] * nums[i]
        # postfix:
        post = 1
        for x in range(len(nums) -1, -1, -1):
            res[x] *= post
            post *= nums[x]

        return res

nums = [1, 2, 3, 4]
s = Solution()
print(s.productExceptSelf(nums))