from collections import defaultdict, deque
from typing import List


def topological_sort(graph) -> list[int]:
    indegree_map = defaultdict(lambda: 0)
    for node, nbrs in graph.items():
        indegree_map[node]
        for nbr in nbrs:
            indegree_map[nbr] += 1
    
    queue = deque()
    for node, indegree in indegree_map.items():
        if indegree == 0:
            queue.append(node)

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph[node]:
            indegree_map[nbr] -= 1
            if indegree_map[nbr] == 0:
                queue.append(nbr)
                
    # If there is a cycle, the order will not contain all nodes
    if len(order) != len(graph):
        return []
    
    return order


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        elif numCourses == 1:
            return [0] if not prerequisites else []
        elif not prerequisites and numCourses > 1:
            return list(range(numCourses))
        
        graph = defaultdict(list)
        for c in range(numCourses): graph[c]
        
        for a, b in prerequisites:
            graph[b].append(a)

        return topological_sort(graph)     
    

# Test cases:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
print(Solution().findOrder(2, [[1,0]]))  # Output: [0, 1]