from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Base case:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        
        @cache
        def solve(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return solve(i+1, j+1)
            
            # Else calculate the operations
            insert = 1 + solve(i, j+1)
            delete = 1 + solve(i+1, j)
            replace = 1 + solve(i+1, j+1)

            return min(insert, delete, replace)

        return solve(0, 0)

# Test cases:
print(Solution().minDistance("horse", "ros"))  # Expected output: 3