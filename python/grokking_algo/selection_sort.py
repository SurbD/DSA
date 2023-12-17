"""
Implemention of the Selection Sort Algorithm
"""


def find_smallest(array):
    """
    Checks an array of len > 0,
    returns the index of the smallest in the array
    """
    if len(array) < 1:
        return None
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    """
    Iterates through and array and sorts elements by 
    adding the smallest element in the array to a new 
    array and does it until the loop terminates
    """
    new_arr = []
    for _ in range(len(array)):
        smallest = find_smallest(array)
        new_arr.append(array.pop(smallest))
    return new_arr


if __name__ == "__main__":
    a_list = [12, 1, 23, 5,32, 22, 22, 87, 45]

    new_list = selection_sort(a_list)
    print(new_list)
