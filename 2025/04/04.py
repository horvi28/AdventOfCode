from grid import Grid

def accessable_papers(grid: Grid) -> int:
    # Iterate through the whole grid and count the accessable elements
    accessable = 0
    for x, y, value in grid:
        if value == '@': # Only the rolls are counts
            neighbours = grid.get_neighbours(x, y)
            if neighbours.count('@') < 4:
                accessable += 1
    return accessable

with open('./2025/04/testinput.txt', 'r') as f:
    lines = f.readlines()
    grid = Grid.from_lines(lines)
    accessable = accessable_papers(grid)

print(f"The accessable roll of papers: {accessable}")