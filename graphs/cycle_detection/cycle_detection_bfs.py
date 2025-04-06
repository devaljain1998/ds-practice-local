from typing import Deque, Set, List
from collections import defaultdict, deque

class Solution:
    def isCycle(self, V, edges):
        # Create graph:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        parent = defaultdict(lambda: -1)
        visited: Set[int] = set()

        def bfs(start):
            queue: Deque[int] = deque()
            queue.append(start)
            visited.add(start)

            while queue:
                node = queue.popleft()
                for nbr in graph[node]:
                    if nbr not in visited:
                        queue.append(nbr)
                        parent[nbr] = node
                        visited.add(nbr)
                    elif parent[node] != nbr:
                        return True
            return False

        # Check for cycles in all components
        for i in range(V):
            if i not in visited:
                if bfs(i):
                    return True
        return False