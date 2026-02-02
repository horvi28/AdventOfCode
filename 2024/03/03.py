import re
from aoc_input import get_input

memory = get_input(2024, 3)
    
#Remove don't() sequences
memory = re.sub(r"don't\(\).*?do\(\)", "", memory, flags=re.DOTALL)

matches = re.finditer(r'mul\((?P<num1>\d+),(?P<num2>\d+)\)', memory)

products = [int(match.group('num1')) * int(match.group('num2')) for match in matches]
print(sum(products))