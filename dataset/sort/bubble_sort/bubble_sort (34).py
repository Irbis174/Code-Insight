from itertools import tee

def bubble_sort(iterable):
    it1, it2 = tee(iterable)
    next(it2, None)
    sorted_iter = [y if x > y else x for x, y in zip(it1, it2)]
    if sorted_iter == list(iterable):
        return sorted_iter
    return bubble_sort(sorted_iter)
