class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Create a min heap
        heap = []
        
        # Initialize the min heap with the pairs
        for i in range(min(k, len(nums1))):
            heap.append((nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        # Convert the list to a heap
        heapq.heapify(heap)
        
        # While the heap is not empty and k pairs are not found
        result = []
        while heap and k > 0:
            # Pop the pair with the smallest sum
            _, u, v, idx2 = heapq.heappop(heap)
            
            # Add the pair to the result list
            result.append([u, v])
            
            # Add the next pairs to the heap
            if idx2 + 1 < len(nums2):
                heapq.heappush(heap, (u + nums2[idx2 + 1], u, nums2[idx2 + 1], idx2 + 1))
            
            k -= 1
        
        return result