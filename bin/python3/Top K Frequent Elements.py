class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)  # Frequency counter
        
        # Create a priority queue (min-heap)
        pq = []
        for num, freq in counter.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        
        # Extract the k most frequent elements from the priority queue
        result = []
        while pq:
            result.append(heapq.heappop(pq)[1])
        
        return result[::-1]  # Reverse the result to get the most frequent elements first