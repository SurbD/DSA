import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = ["Divine", "Hanson", "Jameson"]

def index_of_item(collection, target):
    for index, value in enumerate(collection):
        if target == value:
            return index
    return None

for n in search_names:
    index_ = index_of_item(names, n)
    # print(index_)
