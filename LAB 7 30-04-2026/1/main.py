import heapq
from collections import deque
 
def program1():
    print("=" * 60)
    print("PROGRAM 1 — 8-Puzzle Using Best First Search")
    print("=" * 60)
 
    GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    INITIAL = (1, 2, 3, 4, 0, 6, 7, 5, 8)
 
    def heuristic(state):
        count = 0
        for i in range(9):
            if state[i] != 0 and state[i] != GOAL[i]:
                count += 1
        return count
 
    def get_neighbors(state):
        neighbors = []
        idx = state.index(0)
        row, col = divmod(idx, 3)
        moves = []
        if row > 0: moves.append((-3, "Up"))
        if row < 2: moves.append((3, "Down"))
        if col > 0: moves.append((-1, "Left"))
        if col < 2: moves.append((1, "Right"))
        for delta, direction in moves:
            new_idx = idx + delta
            lst = list(state)
            lst[idx], lst[new_idx] = lst[new_idx], lst[idx]
            neighbors.append((tuple(lst), direction))
        return neighbors
 
    def print_state(state):
        for i in range(0, 9, 3):
            print(" ", state[i], state[i+1], state[i+2])
 
    heap = []
    h0 = heuristic(INITIAL)
    heapq.heappush(heap, (h0, INITIAL, []))
    visited = set()
 
    print(f"\nInitial State: {INITIAL}  h={h0}")
    print_state(INITIAL)
 
    while heap:
        h, state, path = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)
 
        if state == GOAL:
            print(f"\nGoal Reached!")
            print(f"Total moves: {len(path)}")
            print("\nPath taken:")
            cur = INITIAL
            for step, (move, nxt) in enumerate(path, 1):
                print(f"\nMove {step}: {move} -> {nxt}  h={heuristic(nxt)}")
                print_state(nxt)
            return
 
        for neighbor, direction in get_neighbors(state):
            if neighbor not in visited:
                hn = heuristic(neighbor)
                heapq.heappush(heap, (hn, neighbor, path + [(direction, neighbor)]))
 
    print("No solution found.")
    
if __name__ == "__main__":
    program1()