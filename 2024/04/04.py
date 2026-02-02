import numpy as np
from aoc_input import get_input_file

# Read the data into a matrix of characters
input_path = get_input_file(2024, 4)
data = np.genfromtxt(input_path, dtype='str')
data = np.array([list(line) for line in data])

## Helper method to look for the next characters in any direction
# TODO: A lot of parts in the methods are common so probably can be restructured on a better way

def look_north_for_char(pos: tuple, char: str) -> bool:
    # There is no north
    if pos[0] == 0:
        return False, ()
    else:
        new_pos = (pos[0] - 1, pos[1])
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_northeast_for_char(pos: tuple, char: str) -> bool:
    # There is no northeast
    if pos[0] == 0 or pos[1] == (data.shape[1] - 1):
        return False, ()
    else:
        new_pos = (pos[0] - 1, pos[1] + 1)
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_east_for_char(pos: tuple, char: str) -> bool:
    # There is no east
    if pos[1] == (data.shape[0] - 1):
        return False, ()
    else:
        new_pos = (pos[0], pos[1] + 1)
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_southeast_for_char(pos: tuple, char: str) -> bool:
    # There is no southeast
    if pos[0] == (data.shape[0] - 1) or pos[1] == (data.shape[1] - 1):
        return False, ()
    else:
        new_pos = (pos[0] + 1, pos[1] + 1)
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_south_for_char(pos: tuple, char: str) -> bool:
    # There is no south
    if pos[0] == (data.shape[0] - 1):
        return False, ()
    else:
        new_pos = (pos[0] + 1, pos[1])
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_southwest_for_char(pos: tuple, char: str) -> bool:
    # There is no southwest
    if pos[0] == (data.shape[0] - 1) or pos[1] == 0:
        return False, ()
    else:
        new_pos = (pos[0] + 1, pos[1] - 1)
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_west_for_char(pos: tuple, char: str) -> bool:
    # There is no west
    if pos[1] == 0:
        return False, ()
    else:
        new_pos = (pos[0], pos[1] - 1)
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

def look_northwest_for_char(pos: tuple, char: str) -> bool:
    # There is no northwest
    if pos[0] == 0 or pos[1] == 0:
        return False, ()
    else:
        new_pos = (pos[0] - 1, pos[1] - 1)
        if data[new_pos] == char:
            return True, new_pos
        else:
            return False, ()

## Helper methods to look for XMAS in any direction

def look_north_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_north_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to north
        found, new_pos = look_north_for_char(new_pos, 'A')
        if found:
            found, _ = look_north_for_char(new_pos, 'S')
            return found
    return False

def look_northeast_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_northeast_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to northeast
        found, new_pos = look_northeast_for_char(new_pos, 'A')
        if found:
            found, _ = look_northeast_for_char(new_pos, 'S')
            return found
    return False

def look_east_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_east_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to east
        found, new_pos = look_east_for_char(new_pos, 'A')
        if found:
            found, _ = look_east_for_char(new_pos, 'S')
            return found
    return False

def look_southeast_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_southeast_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to southeast
        found, new_pos = look_southeast_for_char(new_pos, 'A')
        if found:
            found, _ = look_southeast_for_char(new_pos, 'S')
            return found
    return False

def look_south_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_south_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to south
        found, new_pos = look_south_for_char(new_pos, 'A')
        if found:
            found, _ = look_south_for_char(new_pos, 'S')
            return found
    return False

def look_southwest_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_southwest_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to southwest
        found, new_pos = look_southwest_for_char(new_pos, 'A')
        if found:
            found, _ = look_southwest_for_char(new_pos, 'S')
            return found
    return False

def look_west_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_west_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to west
        found, new_pos = look_west_for_char(new_pos, 'A')
        if found:
            found, _ = look_west_for_char(new_pos, 'S')
            return found
    return False

def look_northwest_for_xmas(x_pos: tuple) -> bool:
    found, new_pos = look_northwest_for_char(x_pos, 'M')
    if found:
        # From this point we can only go to northwest
        found, new_pos = look_northwest_for_char(new_pos, 'A')
        if found:
            found, _ = look_northwest_for_char(new_pos, 'S')
            return found
    return False

## First part
#
# Strategy will be the following:
# 1. Find first the X-s
# 2. Look in every direction for an M
# 3. If one is found than we can only move into that direction afterwards to look for the other letters
#
# So find all the X-es, and make a index tuple list from it
indices = np.where(data == 'X')
x_list = list(zip(indices[0], indices[1]))

x_mas_counter = 0
for x_pos in x_list:
    # Look for an M in every direction
    if look_north_for_xmas(x_pos):
        x_mas_counter += 1
    if look_northeast_for_xmas(x_pos):
        x_mas_counter += 1
    if look_east_for_xmas(x_pos):
        x_mas_counter += 1
    if look_southeast_for_xmas(x_pos):
        x_mas_counter += 1
    if look_south_for_xmas(x_pos):
        x_mas_counter += 1
    if look_southwest_for_xmas(x_pos):
        x_mas_counter += 1
    if look_west_for_xmas(x_pos):
        x_mas_counter += 1
    if look_northwest_for_xmas(x_pos):
        x_mas_counter += 1
print(f'The answer for the first question: {x_mas_counter}')

## Second part
#
# We are looking for the followings
#
# | M M | M S | S M | S S |
# |  A  |  A  |  A  |  A  |
# | S S | M S | S M | M M |
#
# The common to the aboves that A should be in the middle. So this time we will find all of the A-s instead of the X-s.

## Check diagonals for MAS or SAM

def is_diag1_contains_mas_or_sam(a_pos: tuple) -> bool:
    # Check for MAS
    found, _ = look_northwest_for_char(a_pos, 'M')
    if found:
        # Check the corresponding S in the other direction
        found, _ = look_southeast_for_char(a_pos, 'S')
        if found:
            return True
    # Check for SAM
    found, _ = look_northwest_for_char(a_pos, 'S')
    if found:
        # Check the corresponding M in the other direction
        found, _ = look_southeast_for_char(a_pos, 'M')
        if found:
            return True
    return False

def is_diag2_contains_mas_or_sam(a_pos: tuple) -> bool:
    # Check for MAS
    found, _ = look_northeast_for_char(a_pos, 'M')
    if found:
        # Check the corresponding S in the other direction
        found, _ = look_southwest_for_char(a_pos, 'S')
        if found:
            return True
    # Check for SAM
    found, _ = look_northeast_for_char(a_pos, 'S')
    if found:
        # Check the corresponding M in the other direction
        found, _ = look_southwest_for_char(a_pos, 'M')
        if found:
            return True
    return False

# So find all the A-s and make a index tuple list from it
indices = np.where(data == 'A')
a_list = list(zip(indices[0], indices[1]))

x_mas_counter = 0
for a_pos in a_list:
    if is_diag1_contains_mas_or_sam(a_pos) and is_diag2_contains_mas_or_sam(a_pos):
        x_mas_counter += 1

print(f'The answer for the second question: {x_mas_counter}')