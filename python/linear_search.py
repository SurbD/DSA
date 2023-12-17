def linear_search(array, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for index, value in enumerate(array):
        if value == target:
            return index
    return None

def verify(index):
    if index:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in array.")

numbers = [1,4,2,5,6,3,8,9]

result = linear_search(numbers, 5)
verify(result)
