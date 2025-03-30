from typing import List


def maximum_ways_to_make_change(coins: List[int], n: int) -> int:
    dp = [[0 for _ in range(n + 1)] for _ in range(len(coins) + 1)]
    
    # There will be 1 number of way to make that coin:
    for i in range(len(coins) + 1):
        dp[i][0] = 1
        
    for i in range(1, len(coins) + 1):
        for j in range(1, n + 1):
            
            if coins[i - 1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # import pprint; pprint.pprint(dp, depth=4)
    return dp[len(coins)][n]

# Test cases:
print(maximum_ways_to_make_change([1, 2, 3], 4)) # 4
print(maximum_ways_to_make_change([1, 2, 3], 5)) # 5
print(maximum_ways_to_make_change([2, 5, 3, 6], 10)) # 5
print(maximum_ways_to_make_change([5, 10], 3)) # 0