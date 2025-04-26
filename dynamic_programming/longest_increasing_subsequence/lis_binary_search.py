from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        
        for i in range(n):
            idx = bisect_left(temp, nums[i])
            if idx == len(temp):
                temp.append(nums[i])
            else:
                temp[idx] = nums[i]
        
        return len(temp)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))