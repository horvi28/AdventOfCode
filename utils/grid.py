class Grid:
    def __init__(self, width: int, height: int, default: str = '.'):
        self.width = width
        self.height = height
        self.data = [[default for _ in range(height)] for _ in range(width)]

    # Factory methods to construct the Grid
    @classmethod
    def from_lines(cls, lines: list[str]) -> 'Grid':
        rows = len(lines)
        columns = len(lines[0].rstrip()) if lines else 0
        grid = cls(rows, columns)
        grid.data = [list(line.rstrip()) for line in lines]
        return grid

    @classmethod
    def from_string(cls, text: str) -> 'Grid':
        lines = text.split('\n')
        return cls.from_lines(lines)

    def get(self, x: int, y: int) -> str | None:
        # Range check
        if x in range(0, self.width) and y in range(0, self.height):
            return self.data[x][y]
        else:
            return None

    def set(self, x: int, y: int, char: str) -> None:
        # Range check
        if x in range(0, self.width) and y in range(0, self.height):
            self.data[x][y] = char

    def get_dimensions(self) -> tuple:
        return (self.width, self.height)
    
    def get_row(self, x: int) -> list[str]:
        if x in range(0, self.width):
            return self.data[x]

    def get_column(self, y: int) -> list[str]:
        if y in range(0, self.height):
            return [row[y] for row in self.data]

    def get_upper(self, x: int, y: int) -> str | None:
        return self.get(x + 1, y)
    
    def get_lower(self, x: int, y: int) -> str | None:
        return self.get(x - 1, y)
    
    def get_left(self, x: int, y: int) -> str | None:
        return self.get(x, y - 1)
    
    def get_right(self, x: int, y: int) -> str | None:
        return self.get(x, y + 1)

    def get_upper_left(self, x: int, y: int) -> str | None:
        return self.get(x + 1, y - 1)
    
    def get_upper_right(self, x: int, y: int) -> str | None:
        return self.get(x + 1, y + 1)
    
    def get_lower_left(self, x: int, y: int) -> str | None:
        return self.get(x - 1, y - 1)
    
    def get_lower_right(self, x: int, y: int) -> str | None:
        return self.get(x - 1, y + 1)

    def get_direct_neighbours(self, x: int, y: int) -> list[str | None]:
        upper = self.get_upper(x, y)
        lower = self.get_lower(x, y)
        left = self.get_left(x, y)
        right = self.get_right(x, y)
        return [upper, lower, left, right]
    
    def get_diagonal_neighbours(self, x: int, y: int) -> list[str | None]:
        upper_left = self.get_upper_left(x, y)
        upper_right = self.get_upper_right(x, y)
        lower_left = self.get_lower_left(x, y)
        lower_right = self.get_lower_right(x, y)
        return [upper_left, upper_right, lower_left, lower_right]
    
    def get_neighbours(self, x: int, y: int) -> list[str | None]:
        return self.get_direct_neighbours(x, y) + self.get_diagonal_neighbours(x, y)

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self.data)
