import numpy as np
from aoc_input import get_input

# Plan for the first part:
# Get all the simbols from the map (that is different than '.')
# For loop through the symbols
    # Get the coordinates of the specific symbol
    # Based on that the antinode coordinates can be calculated with the help of coordinate geometry
    # For loop over the antennas, this will be the main antenna for which we check the antinode-s
        # Foor lopp over the other unvisited antenna
        # (they will be marked as visited in the first step, to not check twice the already check pairs)
            # Calculate all the antinodes for the actual antenna:
                # antinode_1 = A1 - _A1A2_
                # antinode_2 = A2 + _A1A2_
                # Check if the points inside the map, otherwise ignore
                # Store them in an array, list or something, but before placing check if the antinode is already exist (can be put into a set or just overwrite)
                # Mark the antenna as visited (later on we don't need to check this antenna again)
    # Calculate the number of antinodes

# In the first part of the puzzle, antinodes only occures when one of the antennas is twice as far away as the other
def calculate_antinode_1(antenna1: np.ndarray, antenna2: np.ndarray) -> None:
    # Calculate the direction vector between the two antenna and calculate the antinodes based on that
    d = antenna2 - antenna1

    antinode1 = antenna1 - d
    antinode2 = antenna2 + d

    add_antinode(antinode1)
    add_antinode(antinode2)


# In the second part, the distance should not be added only once but until it reaches the end of the map
def calculate_antinode_2(antenna1: np.ndarray, antenna2: np.ndarray) -> None:
    # Add the two antenna as antinode
    add_antinode(antenna1)
    add_antinode(antenna2)

    # Calculate the other antinodes
    d = antenna2 - antenna1

    antinode1 = antenna1
    antinode2 = antenna2
    while is_antinode_inside_map(antinode1) or is_antinode_inside_map(antinode2):
        antinode1 = antinode1 - d # -= would make a shallow copy and change antenna1 as well
        antinode2 = antinode2 + d # Same here
        add_antinode(antinode1)
        add_antinode(antinode2)


def is_antinode_inside_map(antinode: np.ndarray) -> bool:
    return antinode[0] < map_size and antinode[1] < map_size and antinode[0] >= 0 and antinode[1] >= 0


def add_antinode(antinode: np.ndarray) -> None:
    # Check if it is fitting into the map
    if is_antinode_inside_map(antinode):
        # Then add it to the map
        antinodes[tuple(antinode)] = True


input = get_input(2024, 8)
lines = input.splitlines()

map =  np.array([list(line.strip()) for line in lines])
print('Initial map:')
print(map)

# Get all the simbols from the map (that is different than '.') and their coordinates
symbols = set(np.unique(map))
symbols.remove('.')
print(symbols)

# Get the size of the map (assuming that it is square matrix)
map_size = map.shape[0]

# Create helper map to store the info if an antenna is visited or not
# And create a map for the antinodes
visited_antennas = np.zeros_like(map, dtype=bool)
antinodes = np.zeros_like(map, dtype=bool)

for symbol in symbols:
    # So find all the antennas with 'symbol' and make a index tuple list from the positions
    antenna_positions = tuple(np.argwhere(map == symbol))

    for antenna1 in antenna_positions:
        print(f'Check antinodes for antenna {antenna1}')
        visited_antennas[tuple(antenna1)] = True
        for antenna2 in antenna_positions:
            # Skip the visited ones (This will also skip 'antenna1' as that is already set to visited)
            if visited_antennas[tuple(antenna2)]:
                continue

            calculate_antinode_2(antenna1, antenna2)
            print('Antinode map:')
            print(antinodes)
num_antinodes = np.count_nonzero(antinodes)
print(f'Overall there is {num_antinodes}')