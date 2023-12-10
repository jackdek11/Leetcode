class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, segments, start, curr):
            if segments == 4:  # Found a valid IP address
                if start == len(s):  # All segments are used and the entire string is consumed
                    ip_addresses.append('.'.join(curr))
                return
            
            # Explore different segment lengths
            for i in range(1, 4):
                if start + i > len(s):
                    break
                
                segment = s[start:start+i]
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    break
                
                curr.append(segment)
                backtrack(s, segments + 1, start + i, curr)
                curr.pop()
        
        ip_addresses = []
        backtrack(s, 0, 0, [])
        return ip_addresses