# Program 2: Find Path Between Two Nodes

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
path = []

def dfs_path(current, destination):
    visited.add(current)
    path.append(current)

    if current == destination:
        return True

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs_path(neighbor, destination):
                return True

    path.pop()
    return False

source = 0
destination = 6

if dfs_path(source, destination):
    print("Path found:", " -> ".join(map(str, path)))
else:
    print("No path found")