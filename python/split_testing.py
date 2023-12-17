def split_list(list_):

    midpoint = len(list_) // 2
    low, high = 0, len(list_)

    left = []
    right = []

    for i in range(low, midpoint):
        left.append(list_[i])
    for j in range(midpoint, high):
        right.append(list_[j])

    return left, right


alist = [2,52, 23, 24, 1, 12, 64, 31]
split = split_list(alist)

print(split)
