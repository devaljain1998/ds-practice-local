from typing import List


def permutations(arr: List[int]) -> List[List[int]]:
    # base case:
    if len(arr) == 1:
        return [arr]
    
    permutation_set = set()
    for i in range(len(arr)):
        element = arr[i]
        
        remaining_arr = arr[:i] + arr[i+1:]
        for p in permutations(remaining_arr):
            permutation_set.add(tuple([element] + p))
    
    return [list(x) for x in permutation_set]

print(sorted(permutations([1, 2, 3])))