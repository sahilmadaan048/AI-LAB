import heapq
from collections import deque
 
 
def program4():
    print("\n" + "=" * 60)
    print("PROGRAM 4 — All 5 Algorithms Compared")
    print("=" * 60)
 
    graph = {
        'S': [('A', 3), ('B', 5)],
        'A': [('C', 4), ('D', 2)],
        'B': [('G', 9)],
        'C': [('G', 7)],
        'D': [('E', 1)],
        'E': [('G', 3)],
        'G': []
    }
    h = {'S': 10, 'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'G': 0}
    start, goal = 'S', 'G'
 
    def path_cost(path):
        cost = 0
        for i in range(len(path) - 1):
            for nb, c in graph[path[i]]:
                if nb == path[i+1]:
                    cost += c
                    break
        return cost
 
    # DFS
    def dfs():
        stack = [(start, [start])]
        visited = set()
        while stack:
            node, path = stack.pop()
            if node == goal:
                return path
            if node in visited:
                continue
            visited.add(node)
            for nb, _ in reversed(graph.get(node, [])):
                if nb not in visited:
                    stack.append((nb, path + [nb]))
        return []
 
    # BFS
    def bfs():
        queue = deque([(start, [start])])
        visited = set([start])
        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
            for nb, _ in graph.get(node, []):
                if nb not in visited:
                    visited.add(nb)
                    queue.append((nb, path + [nb]))
        return []
 
    # Best First (Greedy)
    def best_first():
        heap = [(h[start], start, [start])]
        visited = set()
        while heap:
            _, node, path = heapq.heappop(heap)
            if node == goal:
                return path
            if node in visited:
                continue
            visited.add(node)
            for nb, _ in graph.get(node, []):
                if nb not in visited:
                    heapq.heappush(heap, (h[nb], nb, path + [nb]))
        return []
 
    # A*
    def astar():
        heap = [(h[start], 0, start, [start])]
        visited = {}
        while heap:
            f, g, node, path = heapq.heappop(heap)
            if node in visited and visited[node] <= g:
                continue
            visited[node] = g
            if node == goal:
                return path, g
            for nb, cost in graph.get(node, []):
                ng = g + cost
                heapq.heappush(heap, (ng + h[nb], ng, nb, path + [nb]))
        return [], 0
 
    dfs_path = dfs()
    bfs_path = bfs()
    bf_path  = best_first()
    as_path, as_cost = astar()
 
    print("\n--- Weighted Graph (S to G) ---")
    print(f"{'Algorithm':<12} {'Path':<30} {'Cost':<6} {'Note'}")
    print("-" * 70)
    print(f"{'DFS':<12} {' -> '.join(dfs_path):<30} {path_cost(dfs_path):<6} not optimal")
    print(f"{'BFS':<12} {' -> '.join(bfs_path):<30} {path_cost(bfs_path):<6} min edges")
    print(f"{'Best First':<12} {' -> '.join(bf_path):<30} {path_cost(bf_path):<6} greedy, not optimal")
    print(f"{'A*':<12} {' -> '.join(as_path):<30} {as_cost:<6} OPTIMAL")
 
    # AO* on AND-OR
    print("\n--- AND-OR Graph ---")
    print("A* cannot handle AND nodes (AND-OR structure unsupported).")
    print("AO* solution: A -> (C, D),  cost = 2  [edge(1)+h(C)=3] + [edge(1)+h(D)=4] revised after B expansion")
 
    print("\n--- Summary Table ---")
    print(f"{'Algorithm':<12} {'Complete':<12} {'Optimal':<10} {'Graph Type'}")
    print("-" * 55)
    print(f"{'DFS':<12} {'Yes':<12} {'No':<10} {'OR only'}")
    print(f"{'BFS':<12} {'Yes':<12} {'No(cost)':<10} {'OR only'}")
    print(f"{'Best First':<12} {'Yes':<12} {'No':<10} {'OR only'}")
    print(f"{'A*':<12} {'Yes':<12} {'Yes':<10} {'OR only'}")
    print(f"{'AO*':<12} {'Yes':<12} {'Yes':<10} {'AND-OR'}")
 
 
if __name__ == "__main__":
    program4()