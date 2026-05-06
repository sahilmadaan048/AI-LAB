import heapq

def heuristic(state):
    return abs(2 - state[0])

def get_successors(state):
    x, y = state
    successors = []
    successors.append((4, y))
    successors.append((x, 3))
    successors.append((0, y))
    successors.append((x, 0))
    pour = min(x, 3 - y)
    successors.append((x - pour, y + pour))
    pour = min(y, 4 - x)
    successors.append((x + pour, y - pour))
    return successors

def best_first():
    start = (0,0)
    pq = []
    heapq.heappush(pq, (heuristic(start), start))
    visited = set()
    parent = {}

    while pq:
        _, state = heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)

        if state[0] == 2:
            goal = state
            break

        for s in get_successors(state):
            if s not in visited:
                parent[s] = state
                heapq.heappush(pq, (heuristic(s), s))

    path = []
    while goal != start:
        path.append(goal)
        goal = parent[goal]
    path.append(start)
    path.reverse()

    for p in path:
        print(p)

best_first()