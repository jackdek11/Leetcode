class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        # Create a memoization table to store subproblem results
        memo = [[float('inf')] * n for _ in range(1 << n)]
        
        # Initialize the memoization table with starting points
        for i in range(n):
            memo[1 << i][i] = 0
        
        # Queue to perform BFS
        queue = [(1 << i, i) for i in range(n)]
        
        while queue:
            mask, u = queue.pop(0)
            
            for v in graph[u]:
                new_mask = mask | (1 << v)
                if memo[new_mask][v] > memo[mask][u] + 1:
                    memo[new_mask][v] = memo[mask][u] + 1
                    queue.append((new_mask, v))
        
        # Find the shortest path that visits all nodes
        all_nodes_mask = (1 << n) - 1
        min_path = min(memo[all_nodes_mask][i] for i in range(n))
        
        return min_path