import heapq
from collections import deque
 
 
def program2():
    print("\n" + "=" * 60)
    print("PROGRAM 2 — A* Algorithm on Weighted Graph")
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
    heap = [(h[start], 0, start, [start])]
    visited = {}
 
    explored_order = []
 
    while heap:
        f, g, node, path = heapq.heappop(heap)
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        explored_order.append(node)
 
        if node == goal:
            print(f"\nExplored Order: {' -> '.join(explored_order)}")
            print(f"Optimal Path:   {' -> '.join(path)}")
            print(f"Total Cost    = {g}")
            return
 
        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(heap, (new_f, new_g, neighbor, path + [neighbor]))
 
    print("No path found.")
 

if __name__ == "__main__":
    program2()