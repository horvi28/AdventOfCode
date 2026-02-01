# Plan:
# Find the S where the tachyon enters, mark it's position (row, column)
# Store the column and timeline count in a dictionary, 
#   where the key is the column index, and the value is the timelines for that column
# Jump down 2, see if there is any splitter
# Split the beams (each timeline at a splitter becomes 2 timelines)
# Repeat

from grid import Grid
from aoc_input import get_input

input = get_input(2025, 7)
lines = input.splitlines()
manifold = Grid.from_lines(lines)

# Find S and put into the tachyons dict with 1 timeline
row = 0
index = lines[row].find('S')
tachyons = {}  # key: column index of the beam -> value: number of timelines for that column
tachyons[index] = 1

split_counter = 0
total_rows, toltal_columns = manifold.get_dimensions()
while row <= total_rows - 2:
    row += 2

    # Go through the dict, check if there is any splitter
    old_tachyons = tachyons.copy()
    for column, count in old_tachyons.items():
        # If there is a splitter, then split the beam
        if manifold.get(row, column) == '^':
            split_counter += 1

            # The new column timeline will be the sum of the previous + the new possibilities to end up here
            tachyon_left = column - 1
            tachyons[tachyon_left] = tachyons.get(tachyon_left, 0) + count

            tachyon_right = column + 1
            tachyons[tachyon_right] = tachyons.get(tachyon_right, 0) + count

            # Remove the original position
            del tachyons[column]

timeline_counter = sum(tachyons.values())
print(f'The tachyon beams are splitted {split_counter} times and there are {timeline_counter} timelines')