import sys
import heapq

def dijkstra(graph, src, dst) -> tuple[dict[int, int], dict[int, int]]:
	distance_map = {i:sys.maxsize-1 for i in graph.keys()}
	distance_map[src] = 0

	parent_map = {i:i for i in graph.keys()}

	min_heap = []
	heapq.heappush(min_heap, (0, src))

	while min_heap:
		dist, node = heapq.heappop(min_heap)

		for nbr, wt in graph[node]:
			if dist + wt < distance_map[nbr]:
				# Update distance:
				distance_map[nbr] = dist + wt
				# Add to min heap:
				heapq.heappush(min_heap, (distance_map[nbr], nbr))
				# Update the parent of the node
				parent_map[nbr] = node

	return distance_map, parent_map

def shortest_path(parent_map: dict[int, int], src, dest) -> list[int]:
	curr = dest
	shortest_path = []
	while True:
		shortest_path.append(curr)
		parent = parent_map[curr]
		if curr != parent:
			curr = parent
		else:
			break

	return list(reversed(shortest_path))

def print_shortest_path(V, edges):
	graph = {i:[] for i in range(V)}
	for u, v, wt in edges:
		graph[u].append((v, wt))
		graph[v].append((u, wt))


	distance_map, parent_map = dijkstra(graph, 0, V-1)
	if distance_map[V-1] != (sys.maxsize-1):
		return shortest_path(parent_map, 0, V-1)
	return [-1]

print(print_shortest_path(3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]]))  # Output: [4, 3, 0], [0, 1, 2]

