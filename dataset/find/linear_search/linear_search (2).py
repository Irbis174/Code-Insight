def linear_search(lst, target):
    return next((i for i, val in enumerate(lst) if val == target), -1)
