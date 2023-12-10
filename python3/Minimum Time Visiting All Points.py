import math

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            diagonal_moves = min(dx, dy)
            straight_moves = abs(dx - dy)
            
            total_time += diagonal_moves + straight_moves
            
        return total_time
