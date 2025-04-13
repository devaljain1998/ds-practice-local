# Given a list of tuples
# print it in order: A 0, B 0, A 3, B 3, A 4, B 4, B 5, B 6, A 7, B 7
# using a heap

# Test cases:
import heapq


t1 = [('A', 7), ('B', 0), ('A', 0), ('B', 3), ('A', 3), ('B', 4), ('A', 4), ('B', 5), ('B', 6), ('A', 7)]
# Output: [('A', 0), ('B', 0), ('A', 3), ('B', 3), ('A', 4), ('B', 4), ('B', 5), ('B', 6), ('A', 7), ('B', 7)]

# Sort the list of tuples using the second element
# if they clash, sort by the first element
def comparator(a):
    return a[1], a[0]

# Sort the list of tuples using the comparator
def sort_tuples(tuples):
    min_heap = []
    for t in tuples:
        heapq.heappush(min_heap, (comparator(t), t))
    return [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))]

print(sort_tuples(t1))