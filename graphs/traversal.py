from typing import Dict, List
from collections import deque

def bfs(graph: Dict[int, List[int]], src: int) -> List[int]:
    queue = deque()
    visited = set()
    order = []

    queue.append(src)
    visited.add(src)

    while len(queue) > 0:
        node = queue.popleft()
        # Add to order:
        order.append(node)
        visited.add(node)

        # Add neighbors to queue:
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return order


def dfs(graph, order, visited, src):
    visited.add(src)
    order.append(src)

    for neighbour in graph[src]:
        if neighbour not in visited:
            dfs(graph, order, visited, neighbour)


def dfs_loop(graph, src) -> list:
    visited = set()
    order = []
    stack: deque[int] = deque()

    stack.append(src)
    while len(stack) > 0:
        node = stack.pop()
        visited.add(node)
        order.append(node)

        for nbr in graph[node]:
            if nbr not in visited:
                stack.append(nbr)

    return order


# Test cases:
# Test case 1:
print(bfs({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}, 0))

dfs_order = []
dfs({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}, dfs_order, set(), 0)
print(dfs_order)

print(dfs_loop({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}, 0))