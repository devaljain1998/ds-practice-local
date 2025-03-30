def get_lcs_string(a: str, b: str) -> str:
    n, m = len(a), len(b)
    
    # Create tabulation:
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Use tabulation to print the lcs: 
    lcs_string: str = ''
    i, j = n, m
    while i > 0 and j > 0:
        # If they are equal at the indices then append the char
        # to the lcs string
        if a[i-1] == b[j-1]:
            lcs_string += a[i-1]
            i -= 1
            j -= 1
            
        # else check which is greater, and move in that direction:
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        
        # else move in the above direction
        else:
            j -= 1
    
    return ''.join(reversed(lcs_string))
    
# Test cases:
print(get_lcs_string("abcde", "ace")) # "ace"
print(get_lcs_string("AGGTAB", "GXTXAYB")) # "GTAB"
print(get_lcs_string("abc", "abc")) # "abc"
print(get_lcs_string("abc", "def")) # ""
print(get_lcs_string("ABC", "CBA")) # "A" or "B" or "C"
print(get_lcs_string("AXYT", "AYZX")) # "AY"
print(get_lcs_string("heap", "pea")) # "ea"