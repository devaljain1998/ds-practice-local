from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = 0
        r = k - 1
        
        # Build frequency maps:
        s1freq = defaultdict(lambda: 0)
        freq = defaultdict(lambda: 0)
        for i in range(r + 1):
            freq[s2[i]] += 1
            s1freq[s1[i]] += 1
            
        if freq == s1freq: return True
        
        r += 1
        while r < len(s2):
            freq[s2[r]] += 1
            freq[s2[l]] -= 1
            if freq[s2[l]] == 0:
                del freq[s2[l]]
            
            if s1freq == freq:
                return True
            
            l += 1
            r += 1
    
        return False