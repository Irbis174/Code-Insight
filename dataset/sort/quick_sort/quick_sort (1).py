def quicksort(arr):
    if len(arr) <= 1:
        return arr
    smaller, equal, larger = [], [], []
    pivot = arr[len(arr) // 2]
    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quicksort(smaller) + equal + quicksort(larger)
