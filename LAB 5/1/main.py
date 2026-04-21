# Program 1: BFS Traversal & Tree

from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [2]
}

visited = set()
parent = {}
bfs_order = []

queue = deque()
queue.append(0)
visited.add(0)
parent[0] = None

while queue:
    node = queue.popleft()
    bfs_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = node
            queue.append(neighbor)

print("BFS Order:", *bfs_order)

print("\nBFS Tree (Parent -> Child):")
for node in parent:
    if parent[node] is not None:
        print(f"{parent[node]} -> {node}")