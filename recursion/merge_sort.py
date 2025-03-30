from typing import List


def merge(left: List, right: List) -> List:
    n = len(left)
    m = len(right)
    arr = [None for i in range(n+m)]
    
    i = j = k = 0
    # Merge the two sorted arrays, until one of them is fully merged
    while k < (m+n) and i < n and j < m:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1 
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    # Merge the remaining elements of the left array:
    while i < n and k < (m+n):
        arr[k] = left[i]
        i += 1
        k += 1
        
    # Merge the remaining elements of the right array:
    while j < m and k < (m+n):
        arr[k] = right[j]
        j += 1
        k += 1
        
    return arr
        
    

def merge_sort(start_index: int, end_index: int, arr: List) -> List:
    # Base Condition:
    _size = end_index - start_index
    if _size <= 1:
        return arr[start_index:end_index]
    if _size == 2:
        if arr[start_index] > arr[start_index+1]:
            arr[start_index], arr[start_index+1] = arr[start_index+1], arr[start_index]
        return arr[start_index:end_index]
    
    
    # Recursive Condition:
    mid = (start_index + end_index) // 2
    left = merge_sort(start_index, mid, arr)
    right = merge_sort(mid, end_index, arr)
    
    return merge(left, right)

# Test cases:
arr = [3, 5, 1, 2, 4]
print(merge_sort(0, len(arr), arr))

arr = [3, 5, 1, 2, 4, 6]
print(merge_sort(0, len(arr), arr))

arr = [5, 1, 2]
print(merge_sort(0, len(arr), arr))

arr = [5, 1]
print(merge_sort(0, len(arr), arr))

arr = [5]
print(merge_sort(0, len(arr), arr))

str_arr = ['c', 'a', 'b']
print(merge_sort(0, len(str_arr), str_arr))

str_arr = ['c', 'a', 'b', 'd']
print(merge_sort(0, len(str_arr), str_arr))