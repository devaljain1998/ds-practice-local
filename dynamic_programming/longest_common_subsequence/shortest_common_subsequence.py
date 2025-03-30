def lcs(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    return dp[n][m] 

def shortest_common_subsequence_length(a: str, b: str) -> int:
    return len(a) + len(b) - lcs(a, b)