import os
import requests
from pathlib import Path

def get_input_file(year: int, day: int) -> Path:
    """
    Download the Advent of Code input file if not exist yet and put into the .aoc_cache folder
    
    Args:
        year: Year of the puzzle
        day: Day of the puzzle
    
    Returns:
        String containing the input data
    """
    # Create cache directory in .gitignore'd location
    cache_dir = Path('./.aoc_cache')
    cache_dir.mkdir(exist_ok=True)
    cache_file = cache_dir / f'{year}_{day:02d}_input.txt'
    
    # Return cached input if it exists
    if cache_file.exists():
        return cache_file
    
    # Download from AOC website
    session_cookie = os.environ.get('AOC_SESSION')
    if not session_cookie:
        raise ValueError(
            "AOC_SESSION environment variable not set.\n"
            "Get your session cookie from adventofcode.com."
        )
    
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {'Cookie': f'session={session_cookie}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to download input: {response.status_code} - {response.text}")
    
    # Cache the input
    with open(cache_file, 'w') as f:
        f.write(response.text)
    
    return cache_file

def get_input(year: int, day: int) -> str:
    """
    Retrieve with the puzzle input
    
    Args:
        year: Year of the puzzle
        day: Day of the puzzle
    
    Returns:
        String containing the input data
    """

    input_path = get_input_file(year, day)
    with open(input_path, 'r') as f:
        return f.read()
