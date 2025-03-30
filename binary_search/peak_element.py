from typing import List

minint = float('-inf')

def findPeakElement(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1

    # Check first and last element:
    if nums[0] > nums[1]: return 0
    elif nums[len(nums) - 1] >  nums[len(nums) - 2]: return len(nums) - 1 

    while start <= end:
        mid = start + (end - start) // 2
        preve = nums[mid - 1] if (mid - 1) >= 0 else minint
        nexte = nums[mid + 1] if (mid + 1) < len(nums) else minint

        # Criteria:
        if preve < nums[mid] > nexte:
            return mid
        
        # Change search space:
        if preve >= nums[mid]:
            end = mid - 1
        elif nexte >= nums[mid]:
            start = mid + 1

    return -1

# Test cases:
l1 = [1, 2, 3, 1]
print(l1, "peak element is at index:", findPeakElement(l1))