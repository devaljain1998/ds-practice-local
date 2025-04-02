from typing import List


def solve(prices, i, buy_price, previously_sold, memo) -> int:
    if (i, buy_price, previously_sold) in memo:
        return memo[i, buy_price, previously_sold]

    # reach at the end
    if i == len(prices):
        return 0
    
    # choices:
    # buy the stock
    if buy_price == -1:
        if previously_sold:
            profit = solve(prices, i+1, -1, False, memo) # cooldown
        else:
            profit = max(
                solve(prices, i+1, prices[i], False, memo), # buy
                solve(prices, i+1, -1, False, memo) # cooldown
            )
    
    # sell or hold
    else:
        profit = max(
            solve(prices, i+1, -1, True, memo) + prices[i] - buy_price, #sell
            solve(prices, i+1, buy_price, False, memo)
        )
    
    memo[i, buy_price, previously_sold] = profit
    return profit    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return solve(prices, 0, -1, False, dict())
    
# Test cases:
# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
print(Solution().maxProfit([1,2,3,0,2]))  # Expected output: 3

# Example 2:
# Input: prices = [1]
# Output: 0
print(Solution().maxProfit([1]))  # Expected output: 0

print(Solution().maxProfit([2, 1, 4])) # Expected output: 3