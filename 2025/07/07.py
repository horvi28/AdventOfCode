# Plan:
# Find the S where the tachyon enters, mark it's position (row,column)
# Store the column in a tachyons set (this will make sure that no duplicates)
# Jump down 2, see if there is any splitter
# Split the beams
# Repeat

from grid import Grid

with open('./2025/07/input.txt', 'r') as f:
    lines = f.readlines()
    manifold = Grid.from_lines(lines)

    # Find S and put into the tachyons set
    row = 0
    index = lines[row].find('S')
    tachyons = set()
    tachyons.add(index)

    split_counter = 0
    total_rows, toltal_columns = manifold.get_dimensions()
    while row <= total_rows - 2:
        row += 2

        # Go through the set, check if there is any splitter
        old_tachyons = tachyons.copy()
        for column in old_tachyons:
            # If there is a splitter, then split the beam
            if manifold.get(row, column) == '^':
                tachyons.add(column - 1)
                tachyons.add(column + 1)
                tachyons.remove(column)
                split_counter += 1
print(f'The tachyon beams are splitted {split_counter} times')