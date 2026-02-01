import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup

def get_session_cookie() -> str:
    session_cookie = os.environ.get('AOC_SESSION')
    if not session_cookie:
        raise ValueError(
            "AOC_SESSION environment variable not set.\n"
            "Get your session cookie from adventofcode.com."
        )
    return session_cookie

def parse_for_test_input(response_text: str) -> str | None:
    """
    Parse HTML and extract code blocks
    Usually the first <pre><code> block is the test input
    
    :param response_text: The text of the puzzle which we would like to extract the testinput from
    :return: The extracted test input or None if not found
    """
    soup = BeautifulSoup(response_text, 'html.parser')
    
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            text = code.get_text()
            # Only include if it looks like input data (multiple lines, not inline code)
            if '\n' in text and len(text) > 20:
                return text

    return None

def get_input_file(year: int, day: int, test_input: bool = False) -> Path:
    """
    Download the Advent of Code input file if not exist yet and put into the .aoc_cache folder
    
    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :param test_input: If True the test input is downloaded instead of the unique puzzle input
    :return String containing the input data
    """
    # Create cache directory
    cache_dir = Path('./.aoc_cache')
    cache_dir.mkdir(exist_ok=True)
    test_filename_addition = 'test' if test_input else ''
    cache_filename = f'{year}_{day:02d}_{test_filename_addition}input.txt'
    cache_file = cache_dir / cache_filename
    
    # Return cached input if it exists
    if cache_file.exists():
        return cache_file
    
    # Download from AOC website
    session_cookie = get_session_cookie()

    url = f'https://adventofcode.com/{year}/day/{day}'
    url += '/input' if not test_input else ''
    headers = {'Cookie': f'session={session_cookie}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to download input: {response.status_code} - {response.text}")
    
    # If it is the normal input then we are done, we have directly the input itself
    # If it is a testinput, we still have to parse the code blocks
    input_text = response.text if not test_input else parse_for_test_input(response.text)

    # Cache the input
    with open(cache_file, 'w') as f:
        f.write(input_text)
    
    return cache_file

def get_input(year: int, day: int, test_input: bool = False) -> str:
    """
    Retrieve with the puzzle input or test input based
    
    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :param test_input: If True the test input is returned instead of the unique puzzle input
    :return String containing the input data
    """
    input_path = get_input_file(year, day, test_input)
    with open(input_path, 'r') as f:
        return f.read()
