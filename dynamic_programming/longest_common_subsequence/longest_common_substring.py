def longest_common_substring(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    max_length = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1]==b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    
    return max_length

# Test cases:
print(longest_common_substring("ABC", "ACD")) # 0
# Input: s1 = “GeeksforGeeks”, s2 = “GeeksQuiz” 
# Output : 5 
# Explanation:
# The longest common substring is “Geeks” and is of length 5.
print(longest_common_substring("GeeksforGeeks", "GeeksQuiz")) # 5

# Input: s1 = “abcdxyz”, s2 = “xyzabcd” 
# Output : 4
# Explanation:
# The longest common substring is “abcd” and is of length 4.
print(longest_common_substring("abcdxyz", "xyzabcd")) # 4


# Input: s1 = “abc”, s2 = “” 
# Output : 0.
print(longest_common_substring("abc", "")) # 0