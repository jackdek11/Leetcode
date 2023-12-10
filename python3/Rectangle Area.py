class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = self.calculateRectangleArea(ax1, ay1, ax2, ay2)
        area_b = self.calculateRectangleArea(bx1, by1, bx2, by2)
        overlap_area = self.computeOverlapArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

        return area_a + area_b - overlap_area

    @staticmethod
    def calculateRectangleArea(ax1: int, ay1: int, ax2: int, ay2: int) -> int:
        return abs(ax2 - ax1) * abs(ay2 - ay1)

    def computeOverlapArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        overlap_x1 = max(ax1, bx1)
        overlap_y1 = max(ay1, by1)
        overlap_x2 = min(ax2, bx2)
        overlap_y2 = min(ay2, by2)

        if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
            return self.calculateRectangleArea(overlap_x1, overlap_y1, overlap_x2, overlap_y2)
        else:
            return 0