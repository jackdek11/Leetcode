from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            inDegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)

        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses