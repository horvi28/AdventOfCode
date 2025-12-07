# https://adventofcode.com/2024/day/1

with open('./2024/01/testinput.txt', 'r') as f:
    left_list = []
    right_list = []
    for line in f:
        numbers = line.split()
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))
left_list.sort()
right_list.sort()
sub_list = [abs(b - a) for a, b in zip(left_list, right_list)]

print(sum(sub_list)) # Answer for the first question

similarity_list = [l * right_list.count(l) for l in left_list]

print(sum(similarity_list)) # Answer for the second question