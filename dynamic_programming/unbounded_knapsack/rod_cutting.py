from typing import List


def rod_cutting(prices: List[int], n: int) -> int:
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(len(prices) + 1)]
            
    for i in range(1, len(prices) + 1):
        for j in range(1, n + 1):
            if i <= j:
                dp[i][j] = max(
                    prices[i - 1] + dp[i][j - i], # Include
                    dp[i - 1][j] # Exclude
                )
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[len(prices)][n]

# Test cases:
print(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8)) # 22
print(rod_cutting([3, 5, 8, 9, 10, 17, 17, 20], 8)) # 24
print(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 4)) # 10
print(rod_cutting([1, 10, 3, 1, 3, 1, 5, 9], 8)) # 40