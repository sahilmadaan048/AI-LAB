# Program 4: TSP Brute Force vs Nearest Neighbour

from itertools import permutations

cities = ['A', 'B', 'C', 'D']

dist = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('A', 'D'): 4,
    ('B', 'C'): 5,
    ('B', 'D'): 1,
    ('C', 'D'): 9
}

# Make graph undirected
for (u, v), w in list(dist.items()):
    dist[(v, u)] = w


min_cost = float('inf')
best_path = None

for perm in permutations(['B', 'C', 'D']):

    path = ['A'] + list(perm) + ['A']

    cost = 0

    for i in range(len(path)-1):
        cost += dist[(path[i], path[i+1])]

    if cost < min_cost:
        min_cost = cost
        best_path = path


current = 'A'
unvisited = {'B', 'C', 'D'}

nn_path = ['A']
nn_cost = 0

while unvisited:

    next_city = min(unvisited, key=lambda city: dist[(current, city)])

    nn_cost += dist[(current, next_city)]

    nn_path.append(next_city)

    unvisited.remove(next_city)

    current = next_city

nn_cost += dist[(current, 'A')]
nn_path.append('A')


# ---------------- OUTPUT ----------------

print("Brute Force:")
print("Tour :", " -> ".join(best_path))
print("Cost :", min_cost)

print("\nNearest Neighbour:")
print("Tour :", " -> ".join(nn_path))
print("Cost :", nn_cost)

error = ((nn_cost - min_cost) / min_cost) * 100

print("\nNN Error vs Optimal = {:.1f}%".format(error))