import itertools

cities = ['A', 'B', 'C', 'D']

distance = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

start = 'A'
other_cities = ['B', 'C', 'D']

min_distance = float('inf')
best_route = None

for route in itertools.permutations(other_cities):

    current = start
    total = 0

    for city in route:
        total += distance[current][city]
        current = city

    # Return to starting city
    total += distance[current][start]

    if total < min_distance:
        min_distance = total
        best_route = (start,) + route + (start,)

print("Best Route:", " -> ".join(best_route))
print("Minimum Distance:", min_distance)