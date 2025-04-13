from collections import defaultdict


def is_cycle_present(graph: dict[int, list[int]]) -> bool:
    current_path = set()
    visited = set()
    
    def dfs(node: int) -> bool:
        current_path.add(node)
        visited.add(node)
        
        for nbr in graph[node]:
            if nbr not in visited:
                if dfs(nbr):
                    return True
            elif nbr in current_path:
                return True
            
        current_path.remove(node)
        return False
    
    for node in list(graph.keys()):
        if node not in visited:
            if dfs(node):
                return True
    
    return False

class Solution:
    def isCycle(self, V: int, edges: list[list[int]]) -> bool:
        # Create graph:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
        
        return is_cycle_present(graph)