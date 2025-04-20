from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(lambda: 0)
        l = 0
        r = 0
        max_len = 0
        
        while r < len(s):
            freq[s[r]] += 1
            
            # Condition to increase the left_ptr
            max_freq = max(freq.values())  # find the max_frequency
            conversions = r - max_freq + 1
            # Conversions cannot be greater than k
            while conversions > k and l <= r:
                    freq[s[l]] -= 1
                    l += 1                    
                    max_freq = max(freq.values()) # find the max_frequency:
                    conversions = r - max_freq + 1
                    
            max_len = max(max_len, r-l+1)
            
            # Increase the right_ptr
            r += 1
            
        return max_len
    
print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement('ABAA', 0))