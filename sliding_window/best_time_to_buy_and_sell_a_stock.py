from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        l, r = 0, 0
        while r < len(prices):
            # Condition to increase the left_ptr:
            if prices[l] <= prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            elif not prices[l] <= prices[r]:
                l = r
                
            # Increase the right pointer through out:
            r += 1
            
        return max_profit
                
                    