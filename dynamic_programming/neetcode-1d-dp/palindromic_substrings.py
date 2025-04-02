def is_palindrome(s):
    return s == s[::-1]

def solve(s, start, end, memo) -> int:
    if (start, end) in memo: 
        return memo[start, end]

    if start > end: 
        return 0

    palindromic_substrings = 0
    for i in range(start, end + 1):
        if is_palindrome(s[start:i+1]):  # Check substring directly using slicing
            palindromic_substrings += 1  # Count the current palindrome

    # Add the count of palindromic substrings from the next starting index
    palindromic_substrings += solve(s, start + 1, end, memo)
    
    memo[start, end] = palindromic_substrings
    return palindromic_substrings

print(solve("aaa", 0, 2, {}))  # Expected output: 6
