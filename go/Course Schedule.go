func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make([][]int, numCourses)
	inDegree := make([]int, numCourses)

	for _, prerequisite := range prerequisites {
		course := prerequisite[0]
		prereq := prerequisite[1]

		graph[prereq] = append(graph[prereq], course)
		inDegree[course]++
	}

	queue := make([]int, 0)
	for i := 0; i < numCourses; i++ {
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	count := 0
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		count++

		for _, neighbor := range graph[node] {
			inDegree[neighbor]--
			if inDegree[neighbor] == 0 {
				queue = append(queue, neighbor)
			}
		}
	}

	return count == numCourses
}