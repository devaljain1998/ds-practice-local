def draw_graph_text(graph):
    """
    Draws a simple undirected graph using ASCII characters.
    Assumes graph is a dictionary like {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    """
    from collections import deque

    visited = set()
    levels = {}
    positions = {}

    # BFS to assign levels (depth) to nodes for layout
    def bfs(start):
        queue = deque([(start, 0)])
        while queue:
            node, level = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            levels.setdefault(level, []).append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))

    # Pick the first node as root
    root = next(iter(graph))
    bfs(root)

    # Assign horizontal positions based on level
    for level in sorted(levels):
        for i, node in enumerate(levels[level]):
            positions[node] = (level, i * 5)

    # Build a grid
    max_y = max(y for _, y in positions.values()) + 1
    max_x = max(x for x, _ in positions.values()) + 1
    grid = [[" "] * ((max_y + 1) * 2) for _ in range((max_x + 1) * 2)]

    # Plot nodes
    for node, (x, y) in positions.items():
        grid[x * 2][y * 2] = str(node)

    # Plot edges
    for u in graph:
        for v in graph[u]:
            if u < v:  # Avoid double-drawing
                x1, y1 = positions[u]
                x2, y2 = positions[v]
                x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
                if x1 == x2:
                    for y in range(min(y1, y2) + 1, max(y1, y2)):
                        grid[x1][y] = "—"
                elif y1 == y2:
                    for x in range(min(x1, x2) + 1, max(x1, x2)):
                        grid[x][y1] = "|"
                else:
                    dx = 1 if x2 > x1 else -1
                    dy = 1 if y2 > y1 else -1
                    cx, cy = x1 + dx, y1 + dy
                    while cx != x2 and cy != y2:
                        grid[cx][cy] = "\\"
                        cx += dx
                        cy += dy

    # Print the grid
    for row in grid:
        line = "".join(row).rstrip()
        if line:
            print(line)


# Example usage:
graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
draw_graph_text(graph1)

print("-------------------")
print("-------------------")

graph2 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2]
}
draw_graph_text(graph2)
