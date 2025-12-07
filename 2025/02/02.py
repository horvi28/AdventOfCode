# https://adventofcode.com/2025/day/2

from typing import List

def get_id_ranges(raw_data: str) -> List[list]:
    id_ranges = raw_data.split(',')
    return [[int(boundary) for boundary in id_range.split('-')] for id_range in id_ranges]

def is_invalid(id: int) -> bool:
    id = str(id)
    length = len(id)
    # Only even numbers can be invalid
    if length % 2 == 0:
        middle = int(length / 2)
        first_half = id[: middle]
        second_half = id[middle :]
        return first_half == second_half

with open('./2025/02/input.txt', 'r') as f:
    id_ranges = get_id_ranges(f.readline())

    invalid_sum = 0
    
    # Brute force:
    # Go through all the ranges, and all the numbers and check if they are valid
    for id_range in id_ranges:
        for product_id in range(id_range[0], id_range[1] + 1): # Include the end of the range as well
            if is_invalid(product_id):
                print(f"Invalid product ID has found: {product_id}")
                invalid_sum += product_id

print(f"Sum of invalid product IDs: {invalid_sum}")