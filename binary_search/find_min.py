from typing import List


def findMin(self, nums: List[int]) -> int:
    # Finding the peaks of the left-most and right-most extreme elements:
    if len(nums) == 1: return nums[0]
    
    # Same as find pivot element:
    start = 0
    end = len(nums) - 1

    while start <= end:
        if nums[start] <= nums[end]:
            return nums[start]
        
        mid = start + (end - start) // 2
        element = nums[mid]
        previous_element = nums[mid - 1] if (mid - 1) >= 0 else float('inf')
        next_element = nums[mid + 1] if (mid + 1) < len(nums) else float('inf')

        # min element:
        if previous_element > element < next_element:
            return element
        
        if nums[start] <= element:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

# Test cases:
t1 = [3, 4, 5, 1, 2]
t2 = [4, 5, 6, 7, 0, 1, 2]
t3 = [11, 13, 15, 17]

print("Minimum element in", t1, "is:", findMin(None, t1))
print("Minimum element in", t2, "is:", findMin(None, t2))
print("Minimum element in", t3, "is:", findMin(None, t3))