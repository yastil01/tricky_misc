"""
[1,-2,3,4] = 12
prod = [1, -2, 3,]
max = [1,1,1,1]
min = [1,-2,-6,-24]

[1,-2,-3,4] = 24

input: [-2,3,2,4]
[4,2,3,-2]
A = [-2,-6, -12, -48]
B = [4,8,24,48]
res = [-2, 3, 2]



"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        reverseNums = nums[::-1]
        maxProduct = max(nums[0], nums[-1])
        
        for i in range(1, len(nums)):
            if nums[i-1] != 0:
                nums[i] = nums[i]* nums[i-1]
            if reverseNums[i-1] != 0:
                reverseNums[i] = reverseNums[i]* reverseNums[i-1]
            maxProduct = max(maxProduct, nums[i], reverseNums[i])

        return maxProduct
