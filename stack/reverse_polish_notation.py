from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_fn = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b, 
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)
        }
        stack = deque()

        for t in tokens:
            if t in operator_fn:
                fn = operator_fn[t]
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(fn(n2, n1))
            else:
                stack.append(int(t))
        
        return stack[-1]

# Test cases:
# Test case 1:
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))  # Output: 9

# Test case 2:
tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens))  # Output: 4

# Test case 3:
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens)) # Output: 22