with open('./2025/05/input.txt', 'r') as f:
    fresh_ingredients_ranges = []
    ingredients_coming = False
    fresh_ingredients = 0
    
    for line in f:
        # Until the first blank line the fresh ingredient ID ranges are coming
        if line == "\n":
            ingredients_coming = True
            continue

        if not ingredients_coming:
            # Create a range
            bounds = line.rstrip().split('-')
            lower = int(bounds[0])
            upper = int(bounds[1]) + 1
            fresh_ingredients_ranges.append(range(lower, upper))
        # Then after the first blank line, simply the ingredients are coming
        else:
            ingredient = int(line.rstrip())
            for fresh_range in fresh_ingredients_ranges:
                if ingredient in fresh_range:
                    fresh_ingredients += 1
                    break
print(f"There are {fresh_ingredients} fresh ingredients")