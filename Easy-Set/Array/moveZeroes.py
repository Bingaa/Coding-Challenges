#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j = len(nums) - 1
        while i < j: 
            if nums[i] == 0: 
                nums.append(nums.pop(i))
                j -= 1
            else: 
                i += 1
        