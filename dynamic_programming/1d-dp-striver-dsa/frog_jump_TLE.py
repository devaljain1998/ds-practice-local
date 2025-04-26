"""
Gives TLE
"""


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys


# } Driver Code Ends

from functools import cache

def helper(prev:int, pos: int, n: int, heights: list[int], cache: dict) -> int:
    if (prev, pos) in cache:
        return cache[prev, pos]
        
    if pos == n-1:
        return abs(heights[n-1] - heights[prev])
    
    # Options:
    cost1, cost2 = float('inf'), float('inf')
    # Jump 1 positions:
    if pos + 1 < n:
        cost1 = helper(pos, pos+1, n, heights, cache) + abs(heights[pos]-heights[prev])
    # Jump 2 positions:
    if pos + 2 < n:
        cost2 = helper(pos, pos+2, n, heights, cache) + abs(heights[pos]-heights[prev])
    
    cache[prev, pos] =  min(cost1, cost2)
    return cache[prev, pos]

class Solution:
    def minCost(self, height):
        n = len(height)
        cache = {}
        return min(helper(0, 1, n, height, cache), helper(0, 2, n, height, cache))


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    
    pointer = 0
    
    t = int(input_lines[pointer].strip())
    pointer += 1
    
    for _ in range(t):
        arr = list(map(int, input_lines[pointer].strip().split()))
        pointer += 1
        
        ob = Solution()
        print(ob.minCost(arr))
        print("~")

# } Driver Code Ends