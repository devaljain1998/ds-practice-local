def solve(s, start, memo) -> int:
    if start in memo:
        return memo[start]

    if start == len(s):  # Base case: reached the end of the string
        return 1

    if s[start] == '0':  # Invalid encoding
        return 0 

    # Decode one character
    ans = solve(s, start + 1, memo)

    # Decode two characters if valid
    if start + 1 < len(s) and 10 <= int(s[start:start + 2]) <= 26:
        ans += solve(s, start + 2, memo)

    memo[start] = ans  # Store result in memo
    return ans

class Solution:
    def numDecodings(self, s: str) -> int:
        return solve(s, 0, {})
    
# Test cases:
print(Solution().numDecodings("12"))  # Expected output: 2
print(Solution().numDecodings("226"))  # Expected output: 3
print(Solution().numDecodings("06"))  # Expected output: 0