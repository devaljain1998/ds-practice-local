from typing import List
from collections import deque

def nearest_smaller_to_left(arr: List[int]) -> List[int]:
    answer = [-1 for i in range(len(arr))]
    stack: deque = deque()

    for i in range(len(arr)):
        while len(stack) and not stack[-1][0] < arr[i]:
            stack.pop()

        if len(stack) and stack[-1][0] < arr[i]:
            _, index = stack[-1]
            answer[i] = index
        stack.append((arr[i], i))

    return answer

def nearest_smaller_to_right(arr: List[int]) -> List[int]:
    answer = [len(arr) for i in range(len(arr))]
    stack: deque = deque()

    for i in range(len(arr)-1, -1, -1):
        while len(stack) and not stack[-1][0] < arr[i]:
            stack.pop()

        if len(stack) and stack[-1][0] < arr[i]:
            _, index = stack[-1]
            answer[i] = index
        else:
            stack.append((arr[i], i))


    return answer    

def maximum_area_histogram(heights: List[int]) -> int:
    # Base conditions:
    if len(heights) == 0: return 0
    elif len(heights) == 1: return heights[0]


    left = nearest_smaller_to_left(heights)
    right = nearest_smaller_to_right(heights)

    max_area = 0
    for l, r, height in zip(left, right, heights):
        area = (r - l  - 1) * height
        max_area = max(max_area, area)

    return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return maximum_area_histogram(heights)

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
print(Solution().largestRectangleArea([2,1,5,6,2,3]))

# Input: heights = [2,4]
# Output: 4