graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, 4]
}

def alphabeta(node, alpha, beta, maximizing):
    
    # Leaf node
    if isinstance(node, int):
        return node

    if maximizing:
        value = -float('inf')

        for child in graph[node]:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in graph[node]:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


result = alphabeta('A', -float('inf'), float('inf'), True)

print("Best value:", result)