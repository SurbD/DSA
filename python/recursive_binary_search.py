def recursive_binary_search(array, target):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2

        if array[midpoint] == target:
            return midpoint
        else:
            if array[midpoint] < target:
                return recursive_binary_search(array[midpoint+1:], target)
            else:
                return recursive_binary_search(array[:midpoint-1], target)

def verify(index):
    if index:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in array.")

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10]

    result = recursive_binary_search(numbers, 3)
    verify(result)
