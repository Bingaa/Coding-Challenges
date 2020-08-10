#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(0, len(nums)): 
            if nums[i] in seen: 
                return True 
            seen.add(nums[i])
        
        return False