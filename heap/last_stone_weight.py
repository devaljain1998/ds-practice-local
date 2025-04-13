import heapq


def last_stone_weight(stones: list[int]) -> int:
    max_heap = []
    for stone in stones:
        heapq.heappush(max_heap, -stone)
    
    while len(max_heap) > 1:
        heavy_stone_1 = -heapq.heappop(max_heap)
        heavy_stone_2 = -heapq.heappop(max_heap)
        
        new_stone = heavy_stone_1 - heavy_stone_2
        heapq.heappush(max_heap, -new_stone)
        
    return 0 if len(max_heap) == 0 else -max_heap[0]

# Test cases:
# Test case 1:
print(last_stone_weight([2, 7, 4, 1, 8, 1]))  # Output: 1
# Test case 2:
print(last_stone_weight([1, 3]))  # Output: 2