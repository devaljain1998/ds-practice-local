# Given an array of integers (can contain negative numbers), find the maximum sum of a contiguous subarray.

# Example:
# Input : arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# Output : 7
# The subarray is [4, -1, -2, 1, 5])

# Brute-force: O(n x n), Space complexity: O(0)
# answer = -1
# for i -> n:
#  window_sum = 0
#  for j -> i -> n:
#   window_sum += arr[j]
#   answer = max(window_sum, answer)

# Fixed sized Sliding-window: O(n x n)
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
answer = -1
for window_size in range(1, len(arr) - 1):
    left_ptr, right_ptr = 0, window_size
    window = arr[left_ptr: right_ptr] 
    # [-2] [-3]  -> window_size
    # [-2 -3] [-3 4] -> window_size = 2
    # [-2 -3 4] [-3 4 -1] -> window_size = 3
    
    window_sum = sum(window)
    while right_ptr+1 < len(arr):
        window_sum = window_sum - arr[left_ptr] + arr[right_ptr+1]
        left_ptr += 1
        right_ptr += 1
        
        answer = max(window_sum, answer)
 
# Dynamic Sized Sliding Window: O(n)
# [-2, -3, 4, -1, -2, 1, 5, -3]
# left_ptr = 0, right_ptr = 0
# curr_sum = -2
# right_ptr += 1
# -2 -3 => -5
# left_ptr += 1
# curr_sum = -3
# right_ptr += 1
# curr_sum = -3 + 4 => 1
# right_ptr += 1
# window: -3 4 -1
# curr_sum = 0
# left_ptr += 1
# window: 4 -1
# curr_sum: 3
# right_ptr += 1
# window: 4, -1, -2
# sum: 1
# left_ptr += 1
# window: [-1 -2]
# sum -3
# left_ptr += 1
# window [-2]
# right_ptr += 1
# [-2 1]