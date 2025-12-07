import itertools
from typing import List

def gen_operation(numbers: List[str]):
    operators = ['+', '*', '||']
    for t in itertools.product(operators, repeat=len(numbers) - 1):
        yield ''.join(x + ' ' + y + ' ' for x, y in zip(numbers, t)) + numbers[-1]


def eval_operators(combination: str) -> int:
    a = combination.split()
    total = a[0]
    for i in range(1, len(a) - 1, 2):
        operator = a[i]
        num = a[i + 1]
        if operator == '||':
            total = str(total) + num
        else:
            total = eval(str(total) + operator + num)
    return int(total)


def is_valid_test_value(test_value: int, numbers: List[str]) -> bool:
    # The possible places for the operators alway N - 1 compared to the length of the number list
    # And as + and * the available operators there are 2^N option
    for combination in gen_operation(numbers):
        #print(f'Eval combination: {combination}')

        # We can't use the builtin eval method here as the operators are evaluated left-to-right,
        # the precedence doesn't matter here
        total = eval_operators(combination)
        if total == test_value:
            #print(f'{test_value} can be produced with: {combination}')
            return True
    return False


sum = 0
with open('./2024/07/input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        data = line.split(':')
        test_value = int(data[0])
        numbers = data[1].split()

        #print(f'Test value: {test_value}, numbers: {numbers}')

        if is_valid_test_value(test_value, numbers):
            sum += test_value
print(f'Total sum of the valid test values: {sum}')

