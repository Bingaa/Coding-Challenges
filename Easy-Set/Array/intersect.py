#Given two arrays, write a function to compute their intersection.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Dict = {}
        result = [] 
        for num in nums1: 
            if num in nums1Dict: 
                nums1Dict[num] += 1
            else: 
                nums1Dict[num] = 1 
        
        for num in nums2: 
            if num in nums1Dict: 
                nums1Dict[num] -= 1 
                result.append(num)
                if nums1Dict[num] == 0: 
                    del nums1Dict[num]
        
        return result 