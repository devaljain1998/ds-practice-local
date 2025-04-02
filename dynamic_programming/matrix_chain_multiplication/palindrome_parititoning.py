import sys


def is_palindrome(s: str, i: int, j: int) -> bool:
    # Fix the range to include the character at index j
    return s[i:j+1] == s[i:j+1][::-1]

def solve(s: str, i: int, j: int, memo: list[list[int]]) -> int:
    if i >= j:
        return 0
    
    if is_palindrome(s, i, j):  # Adjusted to check the correct substring
        return 0    
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    min_partitions = sys.maxsize
    for k in range(i, j):  # Ensure the range is correct
        left_partitions = solve(s, i, k, memo)
        right_partitions = solve(s, k+1, j, memo)
        min_partitions = min(min_partitions, left_partitions + right_partitions + 1)
    
    memo[i][j] = min_partitions
    return min_partitions
    

def minimum_cut_to_palidrome_partition(s: str) -> int:
    # Fix memoization table size to match the string length
    memo: list[list[int]] = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return solve(s, 0, len(s) - 1, memo)  # Adjusted range to match 0-based indexing

# Test cases:
# Input: s = "geek" 
# Output: 2 
# Explanation: We need to make minimum 2 cuts, i.e., "g | ee | k".
print(minimum_cut_to_palidrome_partition("geek"))  # Expected output: 2

# Input: s = "aaaa" 
# Output: 0
# Explanation: The string is already a palindrome.
print(minimum_cut_to_palidrome_partition("aaaa"))  # Expected output: 0

# Input: s = "ababbbabbababa" 
# Output: 3
# Explanation: We need to make minimum 3 cuts, i.e., "aba | bb | babbab | aba".
print(minimum_cut_to_palidrome_partition("ababbbabbababa"))  # Expected output: 3

# Input: s = "aab"
# Output: 1
# Explanation: We need to make minimum 1 cut, i.e., "aa | b".
print(minimum_cut_to_palidrome_partition("aab"))  # Expected output: 1

# Input: s = "racecar"
# Output: 0
# Explanation: The string is already a palindrome.
print(minimum_cut_to_palidrome_partition("racecar"))  # Expected output: 0