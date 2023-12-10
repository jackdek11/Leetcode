from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        anagramGroups = []
        
        for string in strs:
            sortedString = "".join(sorted(string))
            stringList = anagrams.get(sortedString)
            
            if stringList is None:
                anagrams[sortedString] = []
            anagrams[sortedString].append(string)
        
        
        for sortedString in anagrams:
            anagramGroups.append(anagrams[sortedString])
        
        return anagramGroups