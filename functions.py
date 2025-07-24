import json
from pathlib import Path

def load_json_to_dict(file_path):
    """
    Load a JSON file and return its content as a dictionary.

    Parameters:
    file_path (str or Path): Path to the JSON file.

    Returns:
    dict: Dictionary containing the JSON content.
    """
    file_path = Path(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def create_output_directory(dir_name: str) -> None:
    """
    Creates the results directory if it does not exist and adds a .gitkeep file.

    Args:
        dir_name (str): Path to the directory.
    """
    print('> Creating directory...')
    print('Directory name:', dir_name)
    dir_path = Path(dir_name)
    if dir_path.exists():
        print('Directory already exists')
    else:
        dir_path.mkdir(parents=True, exist_ok=True)
        print('Directory created')
        # Create an empty .gitkeep file
        gitkeep_path = dir_path / '.gitkeep'
        gitkeep_path.touch()
        print('.gitkeep file created')
    print()