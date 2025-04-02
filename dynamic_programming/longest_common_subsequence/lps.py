def is_palindrome(a) -> bool:
    return a == a[::-1]

def lcs(a, b) -> str:
    n, m = len(a), len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # parse the result
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(result))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if is_palindrome(s): return s
        return lcs(s, s[::-1])        
    
# Test cases:
print(Solution().longestPalindrome("babad"))  # Expected output: "bab" or "aba"
print(Solution().longestPalindrome("abb"))   # Expected output: "bb"
print(Solution().longestPalindrome("cbaacabdkacaabd"))  # Expected output: "aca"