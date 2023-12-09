class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # Array to store the color of each node

        # Perform DFS on each unvisited node
        for i in range(n):
            if colors[i] == -1 and not self.dfs(graph, colors, i, 0):
                return False
        return True

    def dfs(self, graph, colors, node, color):
        colors[node] = color

        # Traverse all adjacent nodes
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False  # Conflicting colors found
            if colors[neighbor] == -1 and not self.dfs(graph, colors, neighbor, 1 - color):
                return False  # Failed to color the neighbor node
        return True