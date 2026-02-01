from aoc_input import get_input

def merge_intervals(intervals: list[list]) -> tuple[list[list], int]:
    """
    It sorts and merges the overlapping intervals given by 'intervals'.
    
    :param intervals: input intervals (they could overlapping)
    :return: With the merged intervals, and the overall number which fits into those intervals
             The result will be a list of intervals in order which are not overlapping at all
    """
    intervals.sort(key=lambda x: x[0])
    
    # Created a merged interval array and start with the first interval
    merged_intervals = [intervals[0]]
    interval_size = 0
    for interval in intervals:
        last_interval = merged_intervals[-1]

        # If the current interval start is smaller then the end of the last interval, they are overlapping
        if interval[0] <= last_interval[1]:
            # Extend the end of the last interval
            last_interval[1] = max(last_interval[1], interval[1])
        else:
            # If they are not overlapping, simply add it to the merged interval list
            # And in the meantime we can also count, how many number fits into that interval
            last_interval_size = last_interval[1] - last_interval[0]
            interval_size += last_interval_size
            merged_intervals.append(interval)
    
    # Add the size of the last interval
    last_interval = merged_intervals[-1]
    last_interval_size = last_interval[1] - last_interval[0]
    interval_size += last_interval_size

    return merged_intervals, interval_size

input = get_input(2025, 5)
lines = input.splitlines()

fresh_ingredients_ranges = []

for line in lines:
    # Until the first blank line the fresh ingredient ID ranges are coming
    if line == "":
        break

    # Create a range
    bounds = line.rstrip().split('-')
    lower = int(bounds[0])
    upper = int(bounds[1]) + 1
    fresh_ingredients_ranges.append([lower, upper])

# Order the intervals and merge them
_, fresh_ids = merge_intervals(fresh_ingredients_ranges)

print(f"Overall there are {fresh_ids} fresh ids")