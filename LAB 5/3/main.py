# Program 3: Detect Cycle Using BFS

from collections import deque

def detect_cycle_bfs(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            queue = deque()
            queue.append((start, -1))
            visited.add(start)

            while queue:
                node, parent = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True
    return False

# Test Case 1: Given Graph
graph1 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [2]
}

if detect_cycle_bfs(graph1):
    print("Cycle detected")
else:
    print("No cycle found")

# Test Case 2: Simple Tree
graph2 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

if detect_cycle_bfs(graph2):
    print("Cycle detected")
else:
    print("No cycle found")