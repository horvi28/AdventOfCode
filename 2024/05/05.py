# https://adventofcode.com/2024/day/5

from typing import List
import numpy as np

def is_rule_violated(update: list, preceding: int, subsequent: int) -> bool:
    return update.index(preceding) > update.index(subsequent)

def is_update_in_correct_order(update: list, rules: List[list]) -> bool:
    for rule in rules:
        if is_rule_violated(update, int(rule[0]), int(rule[1])):
            return False
    return True

rules = []
updates = []
with open('./AdventOfCode/2024/05/input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if '|' in line:
            # This is a rule
            rules.append(list(map(int, line.split('|'))))
        elif ',' in line:
            # This is an update list
            updates.append(list(map(int, line.split(','))))

# Go through the updates
middle_pages_correct = []
middle_pages_uncorrect = []
for update in updates:
    #print(f'Look for rules for pages: {update}')
    # We need only the rules for the pages described by the current update
    filtered_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    if is_update_in_correct_order(update, filtered_rules):
        print(f'{update} is correctly ordered')
        middle_pages_correct.append(update[len(update) // 2])
    else:
        # TODO: I'm not so proud of this part, it uses a lot of heavy array transformation.
        #       It works, but I'm pretty sure that it can be done better. I will rethink it later.
        #
        # Correct the order of the updates
        # If a page is only on the left side of the rules, then it will be the first page
        # If a page is only on the right side of the rules, then it will be the last page
        # Then we can remove these rules from the ruleset and reiterate
        print(f'{update} is incorrectly ordered')

        new_order_pre = []
        new_order_post = []

        # TODO: Either use numpy from the beginning or not use at all
        rule_t = np.array(filtered_rules).transpose()
        index = 0
        while update:
            if index == len(update):
                index = 0
            page = update[index]
            left_side = np.count_nonzero(rule_t[0] == page)
            right_side = np.count_nonzero(rule_t[1] == page)
            if right_side == 0:
                # It is going to the beginning
                new_order_pre.append(page)
                rule_t = rule_t[:, rule_t[0] != page]
                del update[index]
            elif left_side == 0:
                # It is going to the end,
                new_order_post.append(page)
                rule_t = rule_t[:, rule_t[1] != page]
                del update[index]
            else:
                index += 1

        new_order_pre.extend(new_order_post[::-1])
        middle_pages_uncorrect.append(new_order_pre[len(new_order_pre) // 2])


# Summarize the middle pages
print(f'The sum of the middle pages of the currect updates: {sum(middle_pages_correct)}')
print(f'The sum of the middle pages of the not currect updates: {sum(middle_pages_uncorrect)}')