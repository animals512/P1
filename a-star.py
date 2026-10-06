graph = {
    'S': ({'A': 2, 'B': 4}, 5),
    'A': ({'C': 3, 'D': 1}, 3),
    'B': ({'D': 2, 'E': 3}, 4),
    'C': ({'G': 4}, 2),
    'D': ({'G': 5}, 1),
    'E': ({'G': 2}, 3),
    'G': ({}, 0)
}

source = input("Enter source: ").upper()
destination = input("Enter destination: ").upper()

open_list = [source]
closed_list = []
g = {source: 0}
parent = {}

while open_list:

    # Find node with lowest f = g + h
    best = open_list[0]

    for node in open_list:
        f_node = g[node] + graph[node][1]
        f_best = g[best] + graph[best][1]

        if f_node < f_best:
            best = node

    current = best

    print("Current Node:", current)
    print("g =", g[current],
          "h =", graph[current][1],
          "f =", g[current] + graph[current][1])

    if current == destination:
        print("Goal reached!")
        break

    open_list.remove(current)
    closed_list.append(current)

    # Check neighbours
    for neighbour in graph[current][0]:

        cost = graph[current][0][neighbour]
        new_g = g[current] + cost

        if neighbour in closed_list:
            continue

        if neighbour not in open_list:
            open_list.append(neighbour)
            g[neighbour] = new_g
            parent[neighbour] = current

        elif new_g < g[neighbour]:
            g[neighbour] = new_g
            parent[neighbour] = current


# Display path
if current == destination:

    path = []
    node = destination

    while node != source:
        path.append(node)
        node = parent[node]

    path.append(source)
    path.reverse()

    print("\nPath:", " -> ".join(path))
    print("Total Cost:", g[destination])

else:
    print("Path not found")