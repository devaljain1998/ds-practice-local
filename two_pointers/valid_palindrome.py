class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while (left_ptr < right_ptr):
            if s[left_ptr].lower() == s[right_ptr].lower():
                left_ptr += 1
                right_ptr -= 1

            elif s[left_ptr] == ' ' or not s[left_ptr].isalnum():
                left_ptr += 1
                
            elif s[right_ptr] == ' ' or not s[right_ptr].isalnum():
                right_ptr -= 1
                
            else:
                return False
        
        return True

s = Solution()
# test cases:
s1 = "A man, a plan, a canal: Panama"
print(s.isPalindrome(s1)) # True

s2 = "race a car"
print(s.isPalindrome(s2)) # False