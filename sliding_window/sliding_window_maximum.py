from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        
        result = []
        curr_max = max(nums[l:r+1])
        next_max = float('-inf')
        result.append(curr_max)
        l, r = l+1, r+1
        while r < len(nums):
            if nums[l-1] == curr_max:
                curr_max = next_max
            elif nums[r] > curr_max:
                next_max = curr_max
                curr_max = nums[r]
            result.append(curr_max)
            l += 1
            r += 1
        
        return result