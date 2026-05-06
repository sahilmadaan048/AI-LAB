import heapq

def heuristic(state):
    return state[0] + state[1]

def valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    mr = 3 - m
    cr = 3 - c
    if mr > 0 and cr > mr:
        return False
    return True

def successors(state):
    m, c, b = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    result = []
    for dm, dc in moves:
        if b == 'L':
            new = (m-dm, c-dc, 'R')
        else:
            new = (m+dm, c+dc, 'L')
        if valid(new):
            result.append(new)
    return result

def best_first():
    start = (3,3,'L')
    pq = []
    heapq.heappush(pq, (heuristic(start), start))
    visited = set()
    parent = {}

    while pq:
        _, state = heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)

        if state == (0,0,'R'):
            goal = state
            break

        for s in successors(state):
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
    print("Total Steps:", len(path)-1)

best_first()