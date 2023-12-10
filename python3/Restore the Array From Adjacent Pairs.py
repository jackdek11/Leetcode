from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)

        for pair in adjacentPairs:
            u, v = pair
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        start_node = None

        for node, neighbors in adjacency_list.items():
            if len(neighbors) == 1:
                start_node = node
                break

        n = len(adjacentPairs) + 1
        original_array = [0] * n
        original_array[0] = start_node

        visited = set([start_node])

        for i in range(1, n):
            current_node = original_array[i - 1]
            next_node = adjacency_list[current_node][0] if adjacency_list[current_node][0] not in visited else adjacency_list[current_node][1]
            original_array[i] = next_node
            visited.add(next_node)

        return original_array