# Program 4: Topological Sort using DFS

dag = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [4],
    4: [],
    5: [],
    6: []
}

visited = set()
stack = []

def dfs(node):
    visited.add(node)

    for neighbor in dag[node]:
        if neighbor not in visited:
            dfs(neighbor)

    stack.append(node)
 
for node in dag:
    if node not in visited:
        dfs(node)

stack.reverse()

print("Topological Order:", " -> ".join(map(str, stack)))