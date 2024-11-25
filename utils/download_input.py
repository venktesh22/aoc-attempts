import requests
import os
import datetime
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch the session cookie from environment variables
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
BASE_URL = "https://adventofcode.com/{year}/day/{day}/input"

def download_input(day=None, year=None):
    """
    Downloads the input file for the specified day and year from Advent of Code.
    Defaults to today's day and year if not specified.
    """
    # Ensure the session cookie is set
    if not SESSION_COOKIE:
        raise ValueError("Session cookie not found. Please set it in your .env file.")

    # Determine the year
    if year is None:
        year = datetime.datetime.now().year
    elif isinstance(year, str):
        try:
            year = int(year)
        except ValueError:
            raise ValueError("Year must be an integer or a string that can be converted to an integer.")

    # Determine the day
    if day is None:
        day = datetime.datetime.now().day
    elif isinstance(day, str):
        try:
            day = int(day)
        except ValueError:
            raise ValueError("Day must be an integer or a string that can be converted to an integer.")

    # Validate inputs
    if not (1 <= day <= 25):
        raise ValueError("Day must be between 1 and 25.")
    if not (2015 <= year <= datetime.datetime.now().year):
        raise ValueError(f"Year must be between 2015 and {datetime.datetime.now().year} (inclusive).")

    # Create the folder structure
    day_folder = f"{year}/day{day:02d}"
    os.makedirs(day_folder, exist_ok=True)

    # Download the input file
    url = BASE_URL.format(year=year, day=day)
    headers = {"Cookie": f"session={SESSION_COOKIE}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

        # Write the input to a file
        input_path = os.path.join(day_folder, "input.txt")
        with open(input_path, "w") as f:
            f.write(response.text.strip())

        print(f"Input for Year {year}, Day {day:02d} downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download input for Year {year}, Day {day:02d}. Error: {e}")

if __name__ == "__main__":
    import sys

    # Parse command-line arguments
    args = sys.argv[1:]
    day = None
    year = None

    if len(args) >= 1:
        day = args[0]
    if len(args) == 2:
        year = args[1]

    download_input(day, year)
