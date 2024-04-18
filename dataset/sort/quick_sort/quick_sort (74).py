def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return randomized_quicksort(l) + m + randomized_quicksort(r)