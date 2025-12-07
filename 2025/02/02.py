# https://adventofcode.com/2025/day/2

from typing import List

def get_id_ranges(raw_data: str) -> List[list]:
    id_ranges = raw_data.split(',')
    return [[int(boundary) for boundary in id_range.split('-')] for id_range in id_ranges]

def has_repetead_sequence_twice(id: int) -> bool:
    id = str(id)
    length = len(id)
    # Only even numbers can be invalid
    if length % 2 == 0:
        middle = int(length / 2)
        first_half = id[: middle]
        second_half = id[middle :]
        return first_half == second_half

def has_repetead_sequence(id: int) -> bool:
    id = str(id)
    id_length = len(id)
    # It enough to go through the first half of the ID,
    # because after that it can't be repeated
    for sequence_length in range(1, int(id_length / 2) + 1):
        # Test if the length of the sequence is a divisor of the ID length
        # because then it can't be a repeated sequence
        if id_length % sequence_length != 0:
            continue
        # Divide our ID to equal sequence parts
        parts = [id[i : i + sequence_length] for i in range(0, id_length, sequence_length)]
        # check if all the parts are the same
        if(all([part == parts[0] for part in parts])):
            return True
    return False

with open('./2025/02/input.txt', 'r') as f:
    id_ranges = get_id_ranges(f.readline())

    invalid_sum = 0
    
    # Brute force:
    # Go through all the ranges, and all the numbers and check if they are valid
    for id_range in id_ranges:
        for product_id in range(id_range[0], id_range[1] + 1): # Include the end of the range as well
            if has_repetead_sequence(product_id):
                print(f"Invalid product ID has found: {product_id}")
                invalid_sum += product_id

print(f"Sum of invalid product IDs: {invalid_sum}")