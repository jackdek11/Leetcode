class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create a list of tuples where each tuple contains the number of soldiers
        # in a row and the row index
        rows = [(sum(row), i) for i, row in enumerate(mat)]
        
        # Sort the rows based on the number of soldiers and then by row index
        rows.sort(key=lambda x: (x[0], x[1]))
        
        # Extract the row indices of the k weakest rows
        result = [row[1] for row in rows[:k]]
        
        return result
