#Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 1
        for i in range(len(digits) - 1 , -1 , -1): 
            sum += digits[i]
            
            if sum == 10: 
                digits[i] = sum % 10 
                sum = 1
            else: 
                digits[i] = sum
                return digits
        
        digits.insert(0, 1)
        return digits