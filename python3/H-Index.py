class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort in descending order

        h = 0
        for i, citation in enumerate(citations):
            h = max(h, min(i + 1, citation))  # Calculate h as the minimum of (i+1) and citation count
        return h