# Program 2: Find Shortest Path Using BFS

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

source = 0
destination = 6

visited = set()
parent = {}

queue = deque()
queue.append(source)
visited.add(source)
parent[source] = None

found = False

while queue:
    node = queue.popleft()

    if node == destination:
        found = True
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = node
            queue.append(neighbor)

if found:
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    print("Shortest Path found:", " -> ".join(map(str, path)))
else:
    print("No path found")