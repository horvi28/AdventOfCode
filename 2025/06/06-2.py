import math


def get_next_operator(line: str, offset: int) -> tuple[str, int]:
    operators_look_for = ['+', '*']
    for index, character in enumerate(line[offset:], offset):
        if character in operators_look_for:
            return character, index
    return '', -1


def get_vertical_numbers_for_sub_result(lines: list[str], offset: int, number_size) -> list[int]:
    numbers = []
    for digit_index in range(offset, offset + number_size):
        number = ''
        for line in lines:
            number += line[digit_index]
        numbers.append(int(number))
    return numbers


def calculate_sub_result(numbers: list[int], operator: str) -> int:
        if operator == '+':
            sub_result = sum(numbers)
        else:
            sub_result = math.prod(numbers)
        
        print(f'Sub result is {sub_result}')
        return sub_result


with open('./2025/06/input.txt', 'r') as f:
    lines = f.readlines()
    
    # Process the input based on the last line
    # Every column starts with the operator
    operator_row = lines[-1]
    
    offset = 0
    operator = operator_row[0]
    total = 0
    there_are_still_operator = True
    while there_are_still_operator:
        # Find the next operator and offset value
        next_operator, next_offset = get_next_operator(operator_row, offset + 1)
        
        if next_operator != '' and next_offset != -1:
            # Get how long numbers we have in the current sub problem
            # This can be calculated based on the distance between the operators
            # minus one as there is always spaces between the problems
            number_size = next_offset - offset - 1
        else:
            # No more operator, so we are at the end
            # And we also have to calculate the number size differently here
            there_are_still_operator = False
            number_size = len(operator_row) - offset

        # Get the vetical numbers into a list
        numbers = get_vertical_numbers_for_sub_result(lines[:-1], offset, number_size)

        # Calculate the sub result and it to the total
        total += calculate_sub_result(numbers, operator)

        # Prepare for the next iteration
        operator = next_operator
        offset = next_offset
print(f"Total sum of sub results: {total}")