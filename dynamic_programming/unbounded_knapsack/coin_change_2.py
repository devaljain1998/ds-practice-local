from typing import List, Union


def minimum_number_of_coins_for_change(coins: List[int], n: int) -> int:
    dp: List[List[Union[int, float]]] = [[0 for _ in range(n + 1)] for _ in range(len(coins) + 1)]
    
    for i in range(n + 1):
        dp[0][i] = float('inf')
        
    for i in range(n + 1):
        if i % coins[0] == 0:
            dp[1][i] = i // coins[0]
        else:
            dp[1][i] = float('inf')
    
    for i in range(2, len(coins) + 1):
        for j in range(1, n + 1):
            # include or exlcude
            if coins[i - 1] <= j:
                dp[i][j] = min(
                    1 + dp[i][j - coins[i - 1]],
                    dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]
    
    answer: int = int(dp[len(coins)][n]) if not dp[len(coins)][n] == float('inf') else -1
    return answer

# Test cases:
# Input: coins[] = [25, 10, 5], sum = 30
# Output: 2
# Explanation : Minimum 2 coins needed, 25 and 5  
print(minimum_number_of_coins_for_change([25, 10, 5], 30))


# Input: coins[] = [9, 6, 5, 1], sum = 19
# Output: 3
# Explanation: 19 = 9 + 9 + 1
print(minimum_number_of_coins_for_change([9, 6, 5, 1], 19))


# Input: coins[] = [5, 1], sum = 0
# Output: 0
# Explanation: For 0 sum, we do not need a coin
print(minimum_number_of_coins_for_change([5, 1], 0))


# Input: coins[] = [4, 6, 2], sum = 5
# Output: -1
# Explanation: Not possible to make the given sum.
print(minimum_number_of_coins_for_change([4, 6, 2], 5))