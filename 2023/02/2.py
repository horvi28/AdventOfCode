import re

pattern_dict = {
    "red": re.compile("(?P<red>\d*) red"),
    "green": re.compile("(?P<green>\d*) green"),
    "blue": re.compile("(?P<blue>\d*) blue"),
}


def get_cube_num(cubes: str, color: str) -> int:
    m = pattern_dict[color].search(cubes)
    return int(m.group(color)) if m else 0


def is_valid_game(red: int, green: int, blue: int) -> bool:
    max_red_cube = 12
    max_green_cube = 13
    max_blue_cube = 14
    return red <= max_red_cube and green <= max_green_cube and blue <= max_blue_cube


# Part 1
# Checks for game validity, returns with the game ID if valid, 0 otherwise
def check_game_validity(game: str) -> int:
    # Get the game ID first
    game_parts = game.split(":")
    game_id = int(game_parts[0].split(" ")[-1])
    revealed_cubes = game_parts[-1]

    for rc in revealed_cubes.split(";"):
        red = get_cube_num(rc, "red")
        green = get_cube_num(rc, "green")
        blue = get_cube_num(rc, "blue")

        if not is_valid_game(red, green, blue):
            return 0
    return game_id


# Part 2
def fewest_cubes_game(game: str) -> int:
    game_parts = game.split(":")
    revealed_cubes = game_parts[-1]

    red = 0
    green = 0
    blue = 0

    for rc in revealed_cubes.split(";"):
        red = max(red, get_cube_num(rc, "red"))
        green = max(green, get_cube_num(rc, "green"))
        blue = max(blue, get_cube_num(rc, "blue"))

    return red * green * blue


with open("2/input.txt", "r") as f:
    game_id_sum = 0
    for line in f:
        game_id_sum += fewest_cubes_game(line)
    print(game_id_sum)
