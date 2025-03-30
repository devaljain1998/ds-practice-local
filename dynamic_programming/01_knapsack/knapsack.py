from typing import List


def knapsack(profits: List[int], weights: List[int], capacity: int) -> int:
    n = len(weights)
    # Create a matrix of len(items) + 1, capacity + 1:
    cache: List[List[int]] = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                cache[i][j] = max(
                    profits[i - 1] + cache[i - 1][j - weights[i - 1]], # Include
                    cache[i - 1][j] # Exclude
                )
            else:
                cache[i][j] = cache[i - 1][j]

    return cache[n][capacity]

# Test cases:
print(knapsack([1, 2, 3], [4, 5, 1], 4)) # 3
print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)) # 22
print(knapsack([1, 2, 3], [4, 5, 6], 3)) # 0