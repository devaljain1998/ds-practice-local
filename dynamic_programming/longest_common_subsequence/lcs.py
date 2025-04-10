from typing import List


def lcs(a: str, b: str) -> int:
    n, m = len(a), len(b)
    
    dp: List[List[int]] = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])            
            
    return dp[n][m]

print(lcs("ABC", "ACD"))
print(lcs("AGGTAB", "GXTXAYB"))
print(lcs("AXYT", "AYZX"))
print(lcs("ABC", "CBA"))