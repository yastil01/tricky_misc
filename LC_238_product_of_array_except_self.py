class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res = [1] * len(nums)
        mul = 1
        for i in range(len(nums)):
            res[i] = mul * res[i]
            mul = mul * nums[i]
            
        print(res)
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = mul * res[i]
            mul = mul * nums[i]
        
        return res
