# Program 1: DFS Traversal & Tree

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
dfs_order = []

def dfs(node, par=None):
    visited.add(node)
    dfs_order.append(node)
    parent[node] = par

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, node)

dfs(0)

print("DFS Order:", *dfs_order)

print("\nDFS Tree:")
for node in parent:
    if parent[node] is not None:
        print(f"{parent[node]} -> {node}")