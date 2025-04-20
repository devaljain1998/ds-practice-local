from typing import List

def binary_search(arr, start, end, key) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
        
    return -1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range((len(numbers) // 2) + 1):
            other_number = target - numbers[i]
            other_idx = binary_search(numbers, i+1, len(numbers)-1, other_number)
            
            if other_idx != -1:
                return [i+1, other_idx+1]
        
        return []
            
print(Solution().twoSum([2,7,11,15], 9))