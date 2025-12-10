from grid import Grid

def accessable_papers(grid: Grid, remove: bool = False) -> int:
    """
    Count how many roll of papers are accessable by the forklifts 
    and also remove them if 'remove' is set
    
    :param grid: The 2D map where the roll of papers are
    :param remove: If True, the method also removes those roll of papers, by placing an 'x' on that position
    :return: How many roll of papers are accessable
    """
    # Iterate through the whole grid and count the accessable elements
    accessable = 0
    for x, y, value in grid:
        if value == '@': # Only the rolls are counts
            neighbours = grid.get_neighbours(x, y)
            if neighbours.count('@') < 4:
                accessable += 1
                if remove:
                    grid.set(x, y, 'x')
    return accessable

with open('./2025/04/testinput.txt', 'r') as f:
    lines = f.readlines()
    grid = Grid.from_lines(lines)
    total_accessable = 0
    while True:
        # TODO: Make a nice animation here
        print("Map of the roll of papers:")
        print(grid)
        accessable = accessable_papers(grid, True)
        total_accessable += accessable
        print(f"{accessable} roll of paper is accessable.\n")
        if accessable == 0:
            break

print(f"The total accessable roll of papers after removing them: {total_accessable}")