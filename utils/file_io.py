import os

def read_input(file_name, base_path=None):
    """
    Reads the content of the specified file relative to the calling script's directory.

    Args:
        file_name (str): Name of the file (e.g., 'input.txt').
        base_path (str): Base path to look for the file. Defaults to the script's directory.

    Returns:
        str: Content of the file as a single string.
    """
    # If no base path is provided, use the directory of the calling script
    if base_path is None:
        base_path = os.getcwd()

    # Construct the full path to the file
    file_path = os.path.join(base_path, file_name)

    # Read the file
    with open(file_path, "r") as f:
        return f.read().strip()
