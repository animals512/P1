graph = {
    'S': ({'A': 2, 'B': 3}, 4),
    'A': ({'C': 4, 'D': 6}, 2),
    'B': ({'E': 5, 'F': 1}, 3),
    'C': ({}, 5),
    'D': ({}, 2),
    'E': ({}, 4),
    'F': ({}, 0)
}

start = 'S'
goal = 'F'

open_list = [start]
visited = []

while open_list:

    # Find node with smallest heuristic
    best = open_list[0]

    for node in open_list:
        if graph[node][1] < graph[best][1]:
            best = node

    open_list.remove(best)
    visited.append(best)

    print("Visiting:", best, "Heuristic:", graph[best][1])

    if best == goal:
        print("Goal reached!")
        break

    # Add neighbours
    neighbours = graph[best][0]

    for node in neighbours:
        if node not in visited and node not in open_list:
            open_list.append(node)