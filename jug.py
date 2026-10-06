from collections import deque

def water_jug():
    jug1 = 4
    jug2 = 3
    goal = 2

    queue = deque()
    queue.append((0, 0))

    visited = set()
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()

        print("Jug 1:", a, "Jug 2:", b)

        if a == goal or b == goal:
            print("Goal reached!")
            break

        states = [
            (jug1, b),                  # Fill Jug 1
            (a, jug2),                  # Fill Jug 2
            (0, b),                     # Empty Jug 1
            (a, 0),                     # Empty Jug 2

            # Pour Jug 1 -> Jug 2
            (a - min(a, jug2-b), b + min(a, jug2-b)),

            # Pour Jug 2 -> Jug 1
            (a + min(b, jug1-a), b - min(b, jug1-a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

water_jug()