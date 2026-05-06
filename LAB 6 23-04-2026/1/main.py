import heapq

graph = {
    'S': [('A', 3), ('B', 5)],
    'A': [('S', 3), ('C', 4), ('D', 2)],
    'B': [('S', 5), ('D', 6), ('G', 9)],
    'C': [('A', 4), ('G', 7)],
    'D': [('A', 2), ('B', 6), ('E', 1)],
    'E': [('D', 1), ('G', 3)],
    'G': []
}

h = {'S':10,'A':7,'B':6,'C':5,'D':4,'E':2,'G':0}

def best_first(start, goal):
    pq = []
    heapq.heappush(pq,  (h[start], start))
    visited = set()
    parent = {}
    explored = []

    while pq:
        _,  node = heapq.heappop(pq)
        if node in visited:
            continue
        explored.append(node)

        if node == goal:
            break
    
        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                parent[neighbour] = node
                heapq.heappush(pq, (h[neighbour], neighbour))

    path = []
    node = goal 
    total_cost = 0
    while node != start:
        path.append(node)
        p = parent[node]
        for n, c, in graph[p]:
            if n == node:
                total_cost += c
        node = p
    path.append(start)
    path.reverse()

    print("Ecplored path: ", explored)
    print("Path found: ", " -> ".join(path))
    print("Total Path Cost: ", total_cost)

best_first('S', 'G')


# do again with 6 steps