from typing import List

def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
    dp = [1 for _ in range(n)]
    parent = {i:i for i in range(n)}
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    lis = []
    last_index = max(range(n), key=lambda x: dp[x])
    while parent[last_index] != last_index:
        lis.append(arr[last_index])
        last_index = parent[last_index]
    lis.append(arr[last_index])
    
    lis.reverse()
    return lis