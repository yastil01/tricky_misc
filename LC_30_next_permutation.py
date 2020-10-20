class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        
        pivot = length - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1
        
        if pivot < 0:
            return nums.reverse()
        
        i = len(nums) - 1
        while pivot < i:
            if nums[i] > nums[pivot]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
            i -= 1
        
        nums[pivot+1:] = reversed(nums[pivot+1:])
