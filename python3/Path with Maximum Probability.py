class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Initialize distance array
        dist = [0] * n
        dist[start] = 1.0
        
        # Create priority queue
        pq = [(-1.0, start)]
        heapq.heapify(pq)
        
        # Dijkstra's algorithm
        while pq:
            prob, node = heapq.heappop(pq)
            prob *= -1.0
            
            if node == end:
                return prob
            
            if prob < dist[node]:
                continue
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > dist[neighbor]:
                    dist[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0