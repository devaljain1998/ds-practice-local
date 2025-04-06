from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for x, y in connections:
            graph[x].append(y)          # original direction (may need change)
            reverse_graph[y].append(x)  # reverse is fine

        visited = set()
        edges_changed = 0
        
        def dfs(src):
            nonlocal edges_changed
            visited.add(src)
            
            for nbr in graph[src]:  # needs to be reversed
                if nbr not in visited:
                    edges_changed += 1
                    dfs(nbr)
            
            for nbr in reverse_graph[src]:  # correct direction
                if nbr not in visited:
                    dfs(nbr)

        dfs(0)
        return edges_changed

                    
    
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))  # Output: 3

# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 3:
print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))  # Output: 3

# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
print(Solution().minReorder(3, [[1,0],[2,0]]))  # Output: 0


# 6, [[4,5],[0,1],[1,3],[2,3],[4,0]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
print(Solution().minReorder(6, [[4,5],[0,1],[1,3],[2,3],[4,0]]))  # Output: 3