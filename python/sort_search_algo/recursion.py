def sum_(numbers):
    if not numbers: # base case
        return 0

    remaining_sum = sum_(numbers[1:]) # recursive case
    return numbers[0] + remaining_sum

print(sum_([1, 4, 2, 5]))
