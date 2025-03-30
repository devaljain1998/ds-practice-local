# Pivot element which is the smallest element in a rotated sorted array
def find_pivot_element(arr) -> int:
    start = 0
    end = len(arr) - 1
    pivot = -1
    
    # No rotation in the array:
    if arr[start] <= arr[end]:
        return 0 
    
    while start < end:
        # If array is sorted, return start index
        if arr[start] <= arr[end]:
            return start
        
        mid  = (start + end) // 2
        next = (mid + 1) % len(arr)
        prev =  (mid + len(arr) - 1) % len(arr)
        
        # Check if mid is pivot element:
        if  arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        # Check if pivot is in the right of the array:
        # If left half is sorted, pivot must be in right half
        elif arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    return pivot

# Test cases:
l1 = [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(l1, "pivot element is at index:", find_pivot_element(l1))

# sorted array:
l2 = [2, 3, 4, 5, 6, 7, 8, 9]
print(l2, "pivot element is at index:", find_pivot_element(l2))

l3 = [7, 0, 1, 2, 3, 4, 5, 6]
print(l3, "pivot element is at index:", find_pivot_element(l3))