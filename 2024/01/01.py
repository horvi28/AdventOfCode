from aoc_input import get_input

input = get_input(2024, 1)
lines = input.splitlines()

left_list = []
right_list = []
for line in lines:
    numbers = line.split()
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))
left_list.sort()
right_list.sort()
sub_list = [abs(b - a) for a, b in zip(left_list, right_list)]

print(sum(sub_list)) # Answer for the first question

similarity_list = [l * right_list.count(l) for l in left_list]

print(sum(similarity_list)) # Answer for the second question