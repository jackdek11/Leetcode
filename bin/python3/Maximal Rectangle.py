class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        height, left, right = [0] * len(matrix[0]), [0] * len(matrix[0]), [len(matrix[0]) - 1] * len(matrix[0])
        max_area = 0
        for r in range(len(matrix)):
            left_bound = 0
            for c in range(len(matrix[0])):
                if matrix[r][c] == '1':
                    height[c] = height[c] + 1
                    left[c] = max(left[c], left_bound)
                else:
                    left_bound = c + 1
                    left[c] = 0
                    height[c] = 0
            right_bound = len(matrix[0]) - 1
            for c in range(len(matrix[0]) - 1, -1, -1):
                if matrix[r][c] == '1':
                    right[c] = min(right[c], right_bound)
                else:
                    right[c] = len(matrix[0])
                    right_bound = c - 1
                
                max_area = max(max_area, (right[c] - left[c] + 1) * height[c])

        return max_area