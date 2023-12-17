def merge_sort(list_: list) -> list:
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n) time
    """

    if len(list_) <= 1:
        return list_

    left_half, right_half = split(list_)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list_):
    """
    Divide the unsorted list at midpoint and into sublists
    Returns two sublists - left and right

    Takes overall O(log n) time
    """

    midpoint = len(list_) // 2

    low, high = 0, len(list_)
    left = [list_[i] for i in range(low, midpoint)]
    right = [list_[i] for i in range(midpoint, high)]

    # left = list_[:midpoint] # // slicing has a run time of k where k represents the slice size
    # right = list_[midpoint:]

    return left, right

def merge(left: list, right: list) -> list:
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    merged_list = []
    l_index, r_index = 0, 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            merged_list.append(left[l_index])
            l_index += 1
        else:
            merged_list.append(right[r_index])
            r_index += 1

    while l_index < len(left):
        merged_list.append(left[l_index])
        l_index += 1

    while r_index < len(right):
        merged_list.append(right[r_index])
        r_index += 1

    return merged_list


def verify_sorted(list_):
    """
    Iterates through a list and compares the first and second elements of the list
    Returns True if first element is less then second element or 
    if the list contains One or Zero element
    """
    n = len(list_)
    if n in (0, 1):
        return True

    return list_[0] <= list_[1] and verify_sorted(list_[1:])
