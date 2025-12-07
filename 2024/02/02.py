# https://adventofcode.com/2024/day/2

import numpy as np

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

safe_report = 0
with open('./2024/02/input.txt', 'r') as f:
    for line in f:
        report = np.fromstring(line, dtype=int, sep=' ')

        if is_safe(report) or problem_dampener_can_make_it_safe(report):
            print(f'{report}: Safe')
            safe_report += 1
        else:
            print(f'{report}: Unsafe')

    print(f'Number of safe reports: {safe_report}')