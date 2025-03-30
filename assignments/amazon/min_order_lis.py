# lis returns length of the longest
# increasing subsequence in arr of size n
from typing import List


def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom
    # -up manner
    for i in range(1, n):
        for prev in range(0, i):
            if arr[i] > arr[prev]:
                lis[i] = max(lis[i], lis[prev] + 1)

    # Return the maximum of all LIS values
    return max(lis)

def get_remaining_dominoes(domino: List[int], remove: List[int], n) -> List[int]:
    to_be_removed = set(remove[:n+1])
    remaining_dominoes = [domino[i] for i in range(len(domino)) if (i+1) not in to_be_removed]
    return remaining_dominoes

def getMaxPoints(domino, remove, min_order):
    start = 0
    end = len(domino) - 1
    points = 0
    
    while start <= end:
        mid = start + (end - start) // 2
        remaining_dominoes = get_remaining_dominoes(domino, remove, mid)
        
        lis_length = lis(remaining_dominoes)
        if lis_length >= min_order:  # Change condition to >=
            points = max(points, mid + 1)  # Update points correctly
            start = mid + 1
        else:
            end = mid - 1
    return points
            

# STDIN          FUNCTION
# -----          --------
# 4        →     domino[] size n = 4
# 1        →     domino = [1, 2, 3, 4]
# 2
# 3
# 4
# 4        →     remove[] size n = 4
# 3        →     remove = [3, 2, 1, 0]
# 2
# 1
# 0
# 2        →     min_order = 2

# Output:
# 2


# Test cases:
print(getMaxPoints([1, 2, 3, 4], [3, 2, 1, 0], 2)) # 2


# Input:
# 5
# 4
# 5
# 58
# 5
# 4
# 5
# 1
# 0
# 2
# 3
# 4
# 1
# Your Output (stdout)
# 5
# Expected Output
# 4

print(getMaxPoints([4, 5, 58, 5, 4], [5, 1, 0, 2, 3, 4], 1)) # 4


print(getMaxPoints([1, 4, 4, 2, 5, 3], [2, 1, 4, 0, 5, 3], 2)) # 3