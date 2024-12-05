# https://adventofcode.com/2024/day/2

import numpy as np

safe_report = 0
with open('./AdventOfCode/2024/02/input.txt', 'r') as f:
    for line in f:
        report = np.fromstring(line, dtype=int, sep=' ')
        diff = np.diff(report)

        monotonous_increase = np.all(np.logical_and(diff > 0, diff < 4))
        monotonous_decrease = np.all(np.logical_and(diff < 0, diff > -4))
        safe = monotonous_increase or monotonous_decrease
        if safe:
            safe_report += 1
        #print(f'{report} -> Safe? {safe}')

print(f'Number of safe reports: {safe_report}')