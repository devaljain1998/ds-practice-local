import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph:
        graph = {i:[] for i in range(n)}
        for s, d, price in flights:
            graph[s].append((d, price))
        
        prices = [0 if i == src else float('inf') for i in range(n)]
        stops  = [0 if i == src else float('inf') for i in range(n)]
        queue  = [(0, 0, src)]

        while queue:
            _stops, price, node = heapq.heappop(queue)
            if _stops > k + 1:
                continue
            for nbr, wt in graph[node]:
                if price + wt < prices[nbr] and _stops + 1 <= k + 1:
                    stops[nbr]  = _stops + 1
                    prices[nbr] = price + wt
                    heapq.heappush(queue, (stops[nbr], prices[nbr], nbr))
        
        if prices[dst] == float('inf'):
            return -1
        return int(prices[dst])
    
print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))