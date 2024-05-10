def quick_sort_generators(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return list(quick_sort_generator(left)) + [pivot] + list(quick_sort_generator(right))

def quick_sort_generator(arr):
    if len(arr) <= 1:
        yield from arr
    else:
        pivot = arr[0]
        left = (x for x in arr[1:] if x < pivot)
        right = (x for x in arr[1:] if x >= pivot)
        yield from quick_sort_generator(left)
        yield pivot
        yield from quick_sort_generator(right)