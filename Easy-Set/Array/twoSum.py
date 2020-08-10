#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        subtractedNums = {}
        for i in range(0, len(nums)):
            subtractedNumIndex = subtractedNums.get(nums[i])
            if(subtractedNumIndex is None): 
                subtractedNums[target - nums[i]] = i
            else: 
                return [subtractedNumIndex, i]
        
        return []
        