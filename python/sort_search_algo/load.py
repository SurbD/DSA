import os

def load_numbers(filepath):
    """
    Loads numbers from text file, raises an error if file does not exists
    Returns a list of the numbers
    """
    assert os.path.exists(filepath), "File not found, check path"

    with open(filepath, 'r') as file_:
        try:
            numbers = [int(n) for n in file_.readlines()]
        except ValueError as err:
            print(err)
            return None

    return numbers

def load_strings(filepath):
    """
    Loads strings from text file, and raises an error if file does not exists
    Returns a list of the strings from the file
    """
    assert os.path.exists(filepath), "File not found, check file path"

    with open(filepath, 'r') as file:
        strings = [line.strip() for line in file.readlines()]
    return strings
