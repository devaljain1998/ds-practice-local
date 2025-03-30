from typing import List
import copy

def is_palindrome(word: str) -> bool:
    return word == ''.join(reversed(word))

def solve(word: str, start: int, temp_ans: List[str]) -> List[List[str]]:
    # Base condition:
    if start == len(word):
        return [temp_ans]
    
    current_word: str = ''
    final_palindromes: List[List[str]] = []
    for i in range(start, len(word)):
        current_word += word[i]
        
        # Controlled recursion:
        if is_palindrome(current_word):
            # Add word to temp_ans:
            temp_ans.append(current_word)
            
            # recursive:
            result: List[List[str]] = solve(word, i+1, temp_ans)
            final_palindromes.extend(copy.deepcopy(result))
            
            # Remove word from temp_ans:
            temp_ans.pop()
    
    return final_palindromes

    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return solve(s, 0, [])
    

s = Solution()    
# Test Cases:
print(s.partition("aab")) # [["a","a","b"],["aa","b"]]
print(s.partition("a")) # [["a"]]
print(s.partition("aabb")) # [["a","a","b","b"],["a","a","bb"],["aa","b","b"],["aa","bb"]]