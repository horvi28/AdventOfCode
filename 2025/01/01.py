# https://adventofcode.com/2025/day/1

with open('./2025/01/input.txt', 'r') as f:
    dial = 50 # The dial starts at 50
    dial_exactly_at_zero_counter = 0 # Count if the dial stopping exactly at zero
    dial_underflow = 0 # Count if the dial passing zero while rotating to the left
    dial_overflow = 0 # Count if the dial passing zero while rotating to the right
    for line in f:
        line = line.rstrip()
        direction = line[0]
        rotation = int(line[1:])
        
        # Rotate to the dial to the left (lower numbers)
        if direction == 'L':
            # If the dial is exactly at zero, that should not count as underflow, so compensated here
            if dial == 0:
                dial_underflow -= 1
            dial -= rotation
            
            # Handle underflow
            while dial < 0:
                dial += 100
                dial_underflow += 1
        # Rotate the dial to the right (higher numbers)
        else:
            dial += rotation

            # Handle overflow
            while dial > 99:
                dial -= 100
                # 100 is equal with zero, do not count when it finishes at zero
                if dial != 0:
                    dial_overflow += 1

        if dial == 0:
            dial_exactly_at_zero_counter += 1

dial_total_zero_hit = dial_exactly_at_zero_counter + dial_underflow + dial_overflow

print("The dial hit:")
print(f"Exactly zero: {dial_exactly_at_zero_counter}")
print(f"Underflow: {dial_underflow}")
print(f"Overflow: {dial_overflow}")
print(f"Total: {dial_total_zero_hit}")
