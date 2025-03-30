from typing import List

def generate_parenthesis(string: str, open: int, close: int, n: int) -> List[str]:
    # Base Condition:
    if open == 0 and close == 0:
        return [string]
    
    # Recursive condition:
    open_list = []
    closed_list = []
    if close >= open:
        # Choice 1: Add a closing parenthesis
        if close >= 0:
            closed_list = generate_parenthesis(string + ")", open, close - 1, n)
            
        # choice 2: Add an opening parenthesis
        if open >= 0:
            open_list = generate_parenthesis(string + "(", open - 1, close, n)
    
    return open_list + closed_list

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string = "("
        return generate_parenthesis(string, n - 1, n, n)
    
# Test Cases:
solution = Solution()
# test case 1
print("1:", solution.generateParenthesis(1))
print("2:", solution.generateParenthesis(2))
print("3:", solution.generateParenthesis(3))

assert solution.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
assert solution.generateParenthesis()