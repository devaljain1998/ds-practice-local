from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        freq = defaultdict(lambda: 0)
        
        while r < len(s):
            freq[s[r]] += 1
            # Condition to move left_ptr:
            while freq[s[r]] > 1: # duplicate found
                freq[s[l]] -= 1
                l += 1
                
            max_len = max(max_len, r - l + 1)
            # Move right ptr:
            r += 1
        
        return max_len