import numpy as np
import math
from aoc_input import get_input_file

input_path = get_input_file(2025, 6)

problems = np.loadtxt('./2025/06/testinput.txt', dtype=str)
problems_T = problems.transpose()

total = 0
for problem in problems_T:
    numbers = problem[:-1].astype(int)
    operator = problem[-1]
    if operator == '+':
        total += sum(numbers)
    else:
        total += math.prod(numbers)
print(f"Total sum of sub results: {total}")