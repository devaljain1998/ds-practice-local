from typing import List

def find_pivot(nums) -> int:
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        if nums[start] <= nums[end]:
            return start
        
        mid = start + (end - start) // 2
        prev_index = (mid + len(nums) - 1) % len(nums)
        next_index = (mid + 1) % len(nums)
        
        if nums[prev_index] > nums[mid] < nums[next_index]:
            return mid
        
        if nums[start] <= nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

def binary_search_asc(nums, start, end, target) -> int:
    if len(nums) < 3:
        try:
            return nums.index(target)
        except:
            return -1
        
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] ==  target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1

def binary_search_desc(nums, start, end, target) -> int:
    if len(nums) < 3:
        try:
            return nums.index(target)
        except:
            return -1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] ==  target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1


def search(nums: List[int], target: int) -> int:
    pivot_point = find_pivot(nums)
    if pivot_point == -1:
        return binary_search_asc(nums, 0, len(nums) - 1, target)

    left = binary_search_asc(nums, 0, pivot_point - 1, target)
    if left != -1:
        return left
    else:
        return binary_search_asc(nums, pivot_point, len(nums) - 1, target)

# Test cases:
t1, target1 = [4, 5, 6, 7, 0, 1, 2], 0
t2, target2 = [4, 5, 6, 7, 0, 1, 2], 3
t3, target3 = [1], 0
t4, target4 = [3, 5, 1], 5

print("Search for", target1, "in", t1, ":", search(t1, target1))
print("Search for", target2, "in", t2, ":", search(t2, target2))
print("Search for", target3, "in", t3, ":", search(t3, target3))
print("Search for", target4, "in", t4, ":", search(t4, target4)) 