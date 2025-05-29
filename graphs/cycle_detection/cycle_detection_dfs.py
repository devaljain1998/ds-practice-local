from collections import defaultdict
# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
    def isCycle(self, V, edges) -> bool:
        # create graph:
        graph = defaultdict(list[int])
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        
        def dfs(node, parent) -> bool:
            visited.add(node)
            
            for nbr in graph[node]:
                # If neighbour is not visited then recur for that neighbour
                if nbr not in visited:
                    if dfs(nbr, node):
                        return True
                #  If neighbour is visited and is not parent of current node
                # then there is a cycle.
                elif parent != nbr and nbr in visited:
                    return True
                
            return False
            
        return dfs(0, -1)
    
# Test cases:
# 5
# 5
# 0 4
# 1 2
# 1 4
# 2 3
# 3 4
# Expected output: true
print(Solution().isCycle(5, [[0, 4], [1, 2], [1, 4], [2, 3], [3, 4]]))  # Output: True