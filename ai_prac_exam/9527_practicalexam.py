import copy


def get_possible_moves(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    possible_moves = []

    transitions = [
        (1, 0),  
        (2, 0),  
        (0, 1),  
        (0, 2),  
        (1, 1),  
    ]

   
    for transition in transitions:
        m, c = transition  
        if boat_position == 'left':
            new_left_m = left_missionaries - m
            new_left_c = left_cannibals - c
            new_right_m = right_missionaries + m
            new_right_c = right_cannibals + c
            new_boat_position = 'right'
        else:
            new_left_m = left_missionaries + m
            new_left_c = left_cannibals + c
            new_right_m = right_missionaries - m
            new_right_c = right_cannibals - c
            new_boat_position = 'left'

           
        if (
            new_left_m >= 0
            and new_left_c >= 0
            and new_right_m >= 0
            and new_right_c >= 0
            and (new_left_m == 0 or new_left_m >= new_left_c)
            and (new_right_m == 0 or new_right_m >= new_right_c)
        ):
            possible_moves.append(
                (
                    new_left_m,
                    new_left_c,
                    new_right_m,
                    new_right_c,
                    new_boat_position,
                )
            )

    return possible_moves


def depth_limited_search(state, goal, limit, path):
    if state == goal:
        return path  

    if len(path) >= limit:
        return None  

 
    for new_state in get_possible_moves(state):
        if new_state not in path:
            new_path = path + [new_state]
            result = depth_limited_search(new_state, goal, limit, new_path)
            if result:
                return result

    return None  


def iddfs(start, goal, max_depth):
   
    for depth in range(1, max_depth + 1):
        result = depth_limited_search(start, goal, depth, [start])
        if result:
            return result  
    return None  


if __name__ == "__main__":
    
    start_state = (3, 3, 0, 0, 'left')
   
    goal_state = (0, 0, 3, 3, 'right')

   
    solution = iddfs(start_state, goal_state, 20)

    if solution:
        print("Solution found:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found within the depth limit.")

            
    


















































