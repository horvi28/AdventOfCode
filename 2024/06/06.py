# https://adventofcode.com/2024/day/6

import numpy as np
from typing import List, Tuple

def get_path_in_front_of_guard(map: np.array, guard_pos: list, guard_direction: str) -> list:
    if guard_direction == '^':
        return map[0 : guard_pos[0] + 1, guard_pos[1]][::-1]
    elif guard_direction == '>':
        return map[guard_pos[0], guard_pos[1] : ]
    elif guard_direction == 'V':
        return map[guard_pos[0] : , guard_pos[1]]
    else:
        return map[guard_pos[0], 0 : guard_pos[1] + 1][::-1]

def guard_moving_forward(path: list) -> Tuple[int, bool]:
    # The guard is moving forward until it finds an obstacle
    # Find the obstacle closest to the guard
    obstacles = np.where(path == '#')[0]
    if len(obstacles) == 0:
        # There is no obstacle so the guard will leave the mapped area
        index = len(path)
        has_left = True
    else:
        # We need only the first obstacle from the guard point of view
        index = obstacles[0]
        has_left = False

    # The every map-pixel between the obstacle and the guard should be set to visited, including the position of the guard
    visited_path = path[0 : index]
    visited_path[:] = 'X'

    steps_has_been_done = len(visited_path) - 1 # as it is also includes the guard position
    return steps_has_been_done, has_left

def get_new_pos_and_direction(direction: str, pos: List[int], steps: int) -> Tuple[List[int], str]:
    if direction == '^':
        new_direction = '>'
        new_pos = [pos[0] - steps, pos[1]]
    elif direction == '>':
        new_direction = 'V'
        new_pos = [pos[0], pos[1] + steps]
    elif direction == 'V':
        new_direction = '<'
        new_pos = [pos[0] + steps, pos[1]]
    else: # direction == '<'
        new_direction = '^'
        new_pos = [pos[0], pos[1] - steps]
    
    return new_pos, new_direction

with open('./AdventOfCode/2024/06/input.txt', 'rt') as f:
    map =  np.array([list(line.strip()) for line in f.readlines()])
    print('Initial map:')
    print(map)

    # Find the guard
    guard_direction = '^'
    guard_pos = np.squeeze(np.where(map == '^'))

    # The guard is moving forward until it finds an obstacle
    has_left = False
    while not has_left:
        # Get the path ahead from the point of the guard
        path = get_path_in_front_of_guard(map, guard_pos, guard_direction)
        steps, has_left = guard_moving_forward(path)

        # Get the guard new position and direction
        guard_pos, guard_direction = get_new_pos_and_direction(guard_direction, guard_pos, steps)

        print('Map after moving:')
        print(map)
    
    # Count the visited positions
    print(f'Number of visited positions: {np.count_nonzero(map == "X")}')
