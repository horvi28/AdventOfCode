import numpy as np
from aoc_input import get_input

def is_safe(report: list) -> bool:
    diff = np.diff(report)

    monotonous_increase = np.all(np.logical_and(diff > 0, diff < 4))
    monotonous_decrease = np.all(np.logical_and(diff < 0, diff > -4))
    return monotonous_increase or monotonous_decrease

# Brute force
def problem_dampener_can_make_it_safe(report: list) -> bool:
    for i in range(0, len(report)):
        if is_safe(np.delete(report, i)):
            return True
    return False

input = get_input(2024, 2)
lines = input.splitlines()

safe_report = 0
for line in lines:
    report = np.fromstring(line, dtype=int, sep=' ')

    if is_safe(report) or problem_dampener_can_make_it_safe(report):
        print(f'{report}: Safe')
        safe_report += 1
    else:
        print(f'{report}: Unsafe')

print(f'Number of safe reports: {safe_report}')