# https://adventofcode.com/2025/day/3

def get_maximum_joltage(bank: str) -> int:
    # Brute force
    # Test all joltage combination and find the maximum,
    # probably there is a smarter way for this
    maximum_joltage = 0
    for index, digit1 in enumerate(bank):
        for digit2 in bank[index + 1:]:
            joltage_combination = int(digit1 + digit2)
            if joltage_combination > maximum_joltage:
                maximum_joltage = joltage_combination
    return maximum_joltage

with open('./2025/03/input.txt', 'r') as f:
    total_joltage = 0
    for line in f:
        line = line.rstrip()
        maximum_joltage = get_maximum_joltage(line)
        print(f'Maximum joltage for current line {maximum_joltage}')
        total_joltage += maximum_joltage

print(f'Total output joltage: {total_joltage}')
