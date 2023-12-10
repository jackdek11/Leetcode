class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat) # Get the size of the square matrix
        
        # Initialize variables to keep track of diagonal sums
        primary_sum = 0
        secondary_sum = 0
        
        # Loop through each row of the matrix
        for i in range(n):
            # Add the element on the primary diagonal to the primary sum
            primary_sum += mat[i][i]
            # Add the element on the secondary diagonal to the secondary sum
            secondary_sum += mat[i][n-i-1]
        
        # If the matrix has an odd size, subtract the central element from the sum of the diagonals
        if n % 2 == 1:
            middle_index = n // 2
            return primary_sum + secondary_sum - mat[middle_index][middle_index]
        else:
            return primary_sum + secondary_sum