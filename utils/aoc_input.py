import os
import requests
from pathlib import Path

def get_input(year: int, day: int):
    """
    Download or retrieve cached Advent of Code input.
    
    Args:
        year: Year of the puzzle (e.g., 2025)
        day: Day of the puzzle (1-25)
        use_test: If True, looks for testinput.txt locally
    
    Returns:
        String containing the input data
    """
    # Create cache directory in .gitignore'd location
    cache_dir = Path('./.aoc_cache')
    cache_dir.mkdir(exist_ok=True)
    cache_file = cache_dir / f'{year}_{day:02d}_input.txt'
    
    # Return cached input if it exists
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return f.read()
    
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
    
    return response.text