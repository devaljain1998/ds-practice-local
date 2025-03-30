def lcs_table(a: str, b: str) -> list[list[int]]:
    n, m = len(a), len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp

def shortest_common_supersequence(a: str, b: str) -> str:
    n, m = len(a), len(b)
    dp = lcs_table(a, b)
    
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            result.append(a[i-1])
            i -= 1
        else:
            result.append(b[j-1])
            j -= 1    
    
    while i > 0:
        result.append(a[i-1])
        i -= 1
        
    while j > 0:
        result.append(b[j-1])
        j -= 1
        
    return ''.join(reversed(result))

# Test cases:
print(shortest_common_supersequence('abc', 'ab')) # "abc"
print(shortest_common_supersequence('abac', 'cab')) # "cabac"
print(shortest_common_supersequence("geek", "eke")) # "geeke"