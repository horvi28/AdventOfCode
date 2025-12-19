import math

def get_next_operator(line: str, offset: int) -> tuple[str, int]:
    operators_look_for = ['+', '*']
    for index, character in enumerate(line[offset:], offset):
        if character in operators_look_for:
            return character, index
    return '', -1

with open('./2025/06/input.txt', 'r') as f:
    lines = f.readlines()
    
    # Process the input based on the last line
    # Every column starts with the operator
    offset = 0
    operator = lines[-1][0]

    total = 0
    there_are_still_operator = True
    while there_are_still_operator:
        next_operator, next_offset = get_next_operator(lines[-1], offset + 1)
        
        # No more operator, so we are at the end
        if next_operator == '' and next_offset == -1:
            there_are_still_operator = False
            numbers_size = len(lines[-1]) - offset
        else:
            # Get how long numbers we have in the current column
            # This can be calculated based on the distance between the operators
            # minus one as there is always spaces between the columns
            numbers_size = next_offset - offset - 1

        # Get the vetical numbers into a list
        numbers = []
        for digit_index in range(offset, offset + numbers_size):
            number = ''
            for line in lines[:-1]:
                number += line[digit_index]
            numbers.append(int(number))

        # Calculate the sub result
        if operator == '+':
            sub_result = sum(numbers)
        else:
            sub_result = math.prod(numbers)
        total += sub_result
        print(f'Sub result is {sub_result}')

        operator = next_operator
        offset = next_offset
print(f"Total sum of sub results: {total}")