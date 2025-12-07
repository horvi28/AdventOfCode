# https://adventofcode.com/2025/day/1

with open('./2025/01/testinput.txt', 'r') as f:
    dial = 50 # The dial starts at 50
    dial_is_zero_counter = 0
    for line in f:
        line = line.rstrip()
        direction = line[0]
        rotation = int(line[1:])
        
        # Rotate to the dial to the left (lower numbers)
        if direction == 'L':
            dial -= rotation
            
            # Handle underflow
            while dial < 0:
                dial += 100
        # Rotate the dial to the right (higher numbers)
        else:
            dial += rotation

            # Handle overflow
            while dial > 99:
                dial -= 100
        
        if dial == 0:
            dial_is_zero_counter += 1

print(f"The dial has hit zero {dial_is_zero_counter} times")

