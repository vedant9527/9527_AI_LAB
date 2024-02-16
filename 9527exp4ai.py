from collections import deque

def water_jug_bfs(capacity_jug1, capacity_jug2, target):
    visited_states = set()
    initial_state = (0, 0)

    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == target:
            return path

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        jug1, jug2 = current_state

        # Fill jug 1
        if jug1 < capacity_jug1:
            queue.append(((capacity_jug1, jug2), path + ["Fill jug 1"]))

        # Fill jug 2
        if jug2 < capacity_jug2:
            queue.append(((jug1, capacity_jug2), path + ["Fill jug 2"]))

        # Empty jug 1
        if jug1 > 0:
            queue.append(((0, jug2), path + ["Empty jug 1"]))

        # Empty jug 2
        if jug2 > 0:
            queue.append(((jug1, 0), path + ["Empty jug 2"]))

        # Pour water from jug 1 to jug 2
        pour_to_jug2 = min(jug1, capacity_jug2 - jug2)
        if pour_to_jug2 > 0:
            queue.append(((jug1 - pour_to_jug2, jug2 + pour_to_jug2), path + ["Pour jug 1 to jug 2"]))

        # Pour water from jug 2 to jug 1
        pour_to_jug1 = min(jug2, capacity_jug1 - jug1)
        if pour_to_jug1 > 0:
            queue.append(((jug1 + pour_to_jug1, jug2 - pour_to_jug1), path + ["Pour jug 2 to jug 1"]))

    return None

# Example usage:
capacity_jug1 = 4
capacity_jug2 = 3
target = (2, 0)

solution_path = water_jug_bfs(capacity_jug1, capacity_jug2, target)

if solution_path:
    print("Solution found:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")
