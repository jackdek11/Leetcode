func ladderLength(beginWord string, endWord string, wordList []string) int {
    wordSet := make(map[string]bool)
    for _, word := range wordList {
        wordSet[word] = true
    }
    
    if _, ok := wordSet[endWord]; !ok {
        return 0
    }

    ans := 0
    q := []string{beginWord}

    for len(q) > 0 {
        ans++
        size := len(q)
        for i := 0; i < size; i++ {
            wordList := []byte(q[i])
            for j, cache := range wordList {
                for c := 'a'; c <= 'z'; c++ {
                    if rune(cache) == c {
                        continue
                    }
                    wordList[j] = byte(c)
                    word := string(wordList)
                    if word == endWord {
                        return ans + 1
                    }
                    if _, ok := wordSet[word]; ok {
                        q = append(q, word)
                        delete(wordSet, word)
                    }
                }
                wordList[j] = cache
            }
        }
        q = q[size:]
    }

    return 0
}