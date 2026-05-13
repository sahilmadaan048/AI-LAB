# Program 3: TSP Using Brute Force

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

other_cities = ['B', 'C', 'D']

print("Tours:\n")

for perm in permutations(other_cities):

    path = ['A'] + list(perm) + ['A']

    cost = 0

    for i in range(len(path)-1):
        cost += dist[(path[i], path[i+1])]

    print(" -> ".join(path), ":", cost)

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("\nOptimal Tour:")
print(" -> ".join(best_path))

print("Optimal Cost:", min_cost)