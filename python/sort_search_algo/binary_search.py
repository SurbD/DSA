import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = ["Miles", "Hanson", "Kondo"]

def binary_search(collection, target):
    left = 0
    right = len(collection) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if collection[midpoint] == target:
            return midpoint
        if collection[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return None


for name in search_names:
    index = binary_search(names, name)
    # print(index)
