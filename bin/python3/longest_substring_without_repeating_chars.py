class Solution:
    # 5108ms (...yikes)
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = len(s)
        
        max_points = 0
        
        for i in range(len(s)):
            j = i
            local_points = 0
            _locals = []
            while j < end:
                if s[j] not in _locals:
                    local_points +=1
                    _locals.append(s[j])
                    j += 1
                else:
                    break
            max_points = max(local_points, max_points)
        
        return max_points
