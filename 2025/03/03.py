# https://adventofcode.com/2025/day/3

def get_maximum_joltage(battery_bank: str, num_batteries: int) -> int:
    # Okey after thinking a bit
    # Basically we have to select the biggest numbers, 
    # the best of course if the the highest number can make it as the first digit,
    # but if the highest is the last one, that is not much a help.
    # So basically we have to select:
    # - For the first digit we can select all the number except the last one, 
    #   so we need the maximum number in the range (0, len(bank) - (num_batteries - 1))
    # - Then we have to select the maximum number in the range (first_digit_index, len(bank))
    # This logic can be followed similarly if more digit has to be selected
    lower_index = 0
    remaining_digits = num_batteries
    maximum_joltage = ''
    while remaining_digits > 0:
        possible_digits = battery_bank[lower_index : len(battery_bank) - remaining_digits + 1]
        max_digit = max(possible_digits)
        lower_index += possible_digits.index(max_digit) + 1 # The next digit can be only selected starting from this index
        maximum_joltage += max_digit
        remaining_digits -= 1
    return int(maximum_joltage)

with open('./2025/03/input.txt', 'r') as f:
    total_joltage = 0
    for line in f:
        line = line.rstrip()
        maximum_joltage = get_maximum_joltage(line, 12)
        print(f'Maximum joltage for current line {maximum_joltage}')
        total_joltage += maximum_joltage

print(f'Total output joltage: {total_joltage}')
