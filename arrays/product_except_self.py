from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialise prefix and suffix arrays:
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        # Compute pre-fix and suffix arrays:
        #starting from 1st array as prefix product of first element will always be 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        #starting from second last array as suffix product of last element will always be 1
        for i in range(len(nums) - 2, -1, -1): 
            suffix[i] = suffix[i+1] * nums[i+1]

        return [prefix[i]*suffix[i] for i in range(len(nums))]


print(Solution().productExceptSelf([1, 2, 3, 4]))