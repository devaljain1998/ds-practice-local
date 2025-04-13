from collections import defaultdict
import heapq
import sys

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Build graph:
        graph = defaultdict(list[tuple[int, int]])
        for u, v, wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))  # For undirected graph
        
        # Make a minHeap priority queue and put the distance as 0
        # in the priority for the src
        min_heap = []
        heapq.heappush(min_heap, (0, src))
        
        # Distance map:
        distance_list: list[int] = [sys.maxsize - 1 for i in range(V)]
        distance_list[src] = 0
        
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            # Iterate over neighbours:
            for nbr, wt in graph[node]:
                if dist + wt < distance_list[nbr]:
                    distance_list[nbr] = dist + wt
                    heapq.heappush(min_heap, (distance_list[nbr], nbr))                   
        
        return distance_list

# Test cases:
# Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
# Output: [4, 3, 0]
print(Solution().dijkstra(3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 2))  # Output: [4, 3, 0]