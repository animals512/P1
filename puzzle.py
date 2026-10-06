from collections import deque

def solve(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8, 9],
        8: [5, 7, 9],
        9: [7, 8]
    }

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)

        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


start = (1, 2, 3, 4, 5, 6, 8, 7, 9, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

solution = solve(start, goal)

if solution:
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
else:
    print("No solution")