# Read the input create a matrix from it
# 1. going through by rows, find the numbers
#
# ~~~~~~~~~~~~~
# | | | | | | |
# | |x|x|x|x| |
# | |x|1|2|x| | Consiered cells to looking for symbol
# | |x|x|x|x| |
# | | | | | | |
# ~~~~~~~~~~~~~

from aoc_input import get_input

input = get_input(2023, 3)
lines = input.splitlines()