#You are given an n x n 2D matrix representing an image.
#Rotate the image by 90 degrees (clockwise).

#Note:
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix) // 2): 
            for j in range(i, len(matrix[i]) - 1 - i): 
                temp = matrix[i][j] 
                matrix[i][j] = matrix[len(matrix) - 1 - j][i]
                matrix[len(matrix) - 1 - j][i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
                matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = matrix[j][len(matrix) - 1 - i]
                matrix[j][len(matrix) - 1 - i] = temp 