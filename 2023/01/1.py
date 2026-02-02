import re
from aoc_input import get_input

# there is a tricky one where the letters are reused for more digits: eightwothree
numbers_lookup = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def replace_string_digits_to_num(line: str) -> str:
    for ds, dn in numbers_lookup.items():
        line = line.replace(ds, dn)
    return line


pattern_first_digit = re.compile("^\D*(\d)")
pattern_last_digit = re.compile("(\d)\D*$")

input = get_input(2023, 1)
lines = input.splitlines()

sum = 0
for line in lines:
    line = replace_string_digits_to_num(line)
    first_digit = pattern_first_digit.search(line).groups()[0]
    last_digit = pattern_last_digit.search(line).groups()[0]
    calibration_value = int(first_digit + last_digit)
    print(calibration_value)
    sum += calibration_value
print(f"Sum: {sum}")
