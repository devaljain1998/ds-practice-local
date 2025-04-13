from typing import List


def get_left_greatest(arr) -> list[int]:
    ans = [0 for i in range(len(arr))]
    max_till_now = 0
    for i in range(len(arr)):
        ans[i] = max_till_now
        max_till_now = max(arr[i], max_till_now)
    
    return ans

def get_right_greatest(arr) -> list[int]:
    ans = [0 for i in range(len(arr))]
    max_till_now = 0
    for i in range(len(arr)-1, -1, -1):
        ans[i] = max_till_now
        max_till_now = max(arr[i], max_till_now)
    
    return ans


class Solution:
    def trap(self, heights: List[int]) -> int:
        left_greatest = get_left_greatest(heights)
        right_greatest = get_right_greatest(heights)
        rain_waters = [0 for _ in range(len(heights))]
        
        for i, (left_max, right_max, height) in enumerate(zip(left_greatest, right_greatest, heights)):
            rain_waters[i] = max(0, min(left_max, right_max) - height)
        
        return sum(rain_waters)
        
        

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# Input: height = [4,2,0,3,2,5]
# Output: 9