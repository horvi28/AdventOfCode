# https://adventofcode.com/2024/day/3

import re

with open('./AdventOfCode/2024/03/input.txt', 'r') as f:
    memory = f.read()
    
    #Remove don't() sequences
    memory = re.sub(r"don't\(\).*?do\(\)", "", memory, flags=re.DOTALL)

    matches = re.finditer(r'mul\((?P<num1>\d+),(?P<num2>\d+)\)', memory)

    products = [int(match.group('num1')) * int(match.group('num2')) for match in matches]
    print(sum(products))
    pass