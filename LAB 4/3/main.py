# Program 3: Detect Cycle in Undirected Graph

def detect_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
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

if detect_cycle(graph1):
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

if detect_cycle(graph2):
    print("Cycle detected")
else:
    print("No cycle found")