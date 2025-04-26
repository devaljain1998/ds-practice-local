#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys


# } Driver Code Ends

from functools import cache

#User function Template for python3
class Solution:
    def minCost(self, height):
        
        @cache
        def helper(pos: int) -> int:
            # base condition:
            if pos == 0:
                return 0
            
            cost1, cost2 = float('inf'), float('inf')
            
            if pos - 1 >= 0:
                cost1 = helper(pos-1) + abs(height[pos]-height[pos-1])
            if pos - 2 >= 0:
                cost2 = helper(pos-2) + abs(height[pos]-height[pos-2])
                
            return min(cost1, cost2)
        
        return helper(len(height) - 1)


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