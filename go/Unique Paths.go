func uniquePaths(m int, n int) int {
    myList := make([][]int, m)
    for i := 0; i < m; i++ {
        myList[i] = make([]int, n)
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i == 0 || j == 0 {
                myList[i][j] = 1
            } else {
                myList[i][j] = myList[i-1][j] + myList[i][j-1]
            }
        }
    }

    return myList[m-1][n-1]
}