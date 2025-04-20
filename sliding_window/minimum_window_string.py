from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(lambda: 0)
        for c in t: mp[c] += 1

        # count of distinct keys in map:
        count = len(mp)
        l = 0
        r = 0
        answer: list = []
        while r < len(s):
            char = s[r]
            # if we need that char in map:
            if char in mp:
                mp[char] -= 1
                if mp[char] == 0:
                    count -= 1
            
            # Condition for answer
            # Try to shrink to find if we can have more answers:
            while count == 0:
                # update answer
                answer = [l, r]

                lchar = s[l]
                if lchar in mp:
                    mp[lchar] += 1
                    if mp[lchar] > 0:
                        count += 1
                l += 1

            r += 1

        return s[answer[0]:answer[1]+1] if answer else ''

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow('a', 'aa'))