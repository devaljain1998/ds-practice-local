from collections import defaultdict, deque
from typing import DefaultDict


def topological_sort(graph: dict[int, list[int]]) -> list[int]:
    indegree_dict: DefaultDict[int, int] = defaultdict(int)
    for vertex, nbrs in graph.items():
        indegree_dict[vertex]
        for nbr in nbrs:
            indegree_dict[nbr] += 1
    
    order: list[int] = []
    queue: deque[int] = deque()
    # Insert 0 indegree vertices into the queue:
    for vertex, indegree in indegree_dict.items():
        if indegree == 0:
            queue.append(vertex)
    
    while len(queue):
        vertex = queue.popleft()
        for nbr in graph[vertex]:
            indegree_dict[nbr] -= 1
            if indegree_dict[nbr] == 0:
                queue.append(nbr)
        order.append(vertex)
        
    return order


# Test cases:
# Test case 1: Simple directed graph
graph1 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(topological_sort(graph1))
    
        