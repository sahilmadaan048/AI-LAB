# Program 4: Connected Components Using BFS

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
component_number = 1

for node in graph:
    if node not in visited:
        queue = deque()
        queue.append(node)
        visited.add(node)

        component_nodes = []

        while queue:
            current = queue.popleft()
            component_nodes.append(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(f"Connected Component {component_number}:", *component_nodes)
        component_number += 1