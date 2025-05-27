# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

from typing import List
from collections import defaultdict


def three_sum(nums: List[int]) -> List[List[int]]:
    # Sort the array: nums.sort()
    # freq[n] += 1
    # start iterating for i in 0 -> n-2
    # for j in i+1 -> n-1
    # nums[i] + nums[j] + nums[k] = 0
    # target / nums[k] = - (nums[i] + nums[j])
    # check in my freq whether target is there or not
    # if yes then I am gonna add it to my answer set:
    
    # sort the array
    nums.sort() # O 
    
    # calculate a frequency array:
    freq = {} # -1: 2, 0:1, 1:1 ...
    for n in nums: 
        if n not in freq:
            freq[n] = 0
        freq[n] += 1
    
    
    ans_set = set()
    # O (n)
    for i in range(len(nums) - 1):
        freq[nums[i]] -= 1
        # O (m)
        for j in range(len(nums)-2):
            target = -(nums[i] + nums[j])
            freq[nums[j]] -= 1
            
            # Check whether target is there in freq or not:
            if target in freq and freq[target] > 0:
                ans_set.add(tuple(sorted([nums[i], nums[j], target])))
            
            # backtrack
            freq[nums[j]] += 1
        # backtrack
        freq[nums[i]] += 1
        
    ans_list = list(map(lambda s: list(s), ans_set))
    return ans_list


def three_sum_optimised(nums) -> list:
    left_ptr = 0
    right_ptr = len(nums) - 1
    
    freq = {}
    for n in nums:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1
    
    ans_set = set()
    while left_ptr < right_ptr:
        target = - (nums[left_ptr] + nums[right_ptr])
        
        freq[nums[left_ptr]] -= 1
        freq[nums[right_ptr]] -=  1
        
        # Found the answer:
        if target in freq and freq[target] > 0:
            ans_set.add(tuple(sorted([nums[left_ptr], nums[right_ptr], target])))
            freq[nums[left_ptr]] += 1
            left_ptr += 1
        # Couldn't find the answer:
        else:
            if nums[left_ptr] + nums[right_ptr] > 0:
                freq[nums[left_ptr]] += 1
                left_ptr += 1
            else:
                freq[nums[right_ptr]] += 1
                right_ptr -= 1
        
    ans_list = list(map(lambda s: list(s), ans_set))
    return ans_list



# O (n x m) => O (n2) n2 + nlogn => O (n2)
# print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum_optimised([-1,0,1,2,-1,-4]))