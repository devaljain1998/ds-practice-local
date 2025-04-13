from typing import List


def is_cycle_present(graph: dict[int, list[int]]) -> set:
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
            # Perform DFS on the node
            # To keep filling the current path
            dfs(node)
    
    return current_path

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        graph = {}
        for i, adj_list in enumerate(adj):
             graph[i] = adj_list
        # Get all nodes in the cycle
        cycle_nodes = is_cycle_present(graph)
        # Get all nodes that are not in the cycle
        safe_nodes = set(range(V)) - cycle_nodes
        # Return the sorted list of safe nodes
        return sorted(safe_nodes)