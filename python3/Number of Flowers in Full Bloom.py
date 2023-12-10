import heapq

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Step 1: Create a list of tuples with start time, end time, and index
        flower_times = [(start, end, i) for i, (start, end) in enumerate(flowers)]
        # Step 2: Sort the list based on start time
        flower_times.sort()

        n = len(flowers)
        m = len(people)
        result = [0] * m
        bloom_heap = []

        i = 0  # Index for flower_times
        for person_arrival in sorted(enumerate(people), key=lambda x: x[1]):
            person_idx, person_time = person_arrival

            # Step 3: Add flowers to bloom_heap that are in bloom at person's arrival time
            while i < n and flower_times[i][0] <= person_time:
                _, end_time, flower_idx = flower_times[i]
                heapq.heappush(bloom_heap, (end_time, flower_idx))
                i += 1

            # Step 4: Pop flowers from bloom_heap whose end time has passed
            while bloom_heap and bloom_heap[0][0] < person_time:
                heapq.heappop(bloom_heap)

            # Step 5: Count the number of flowers currently in bloom for the person
            result[person_idx] = len(bloom_heap)

        return result