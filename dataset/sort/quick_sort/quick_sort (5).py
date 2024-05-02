def quicksort(arr):
    if len(arr) <= 1:
        return arr
    smaller, equal, larger = partition(arr)
    return quicksort(smaller) + equal + quicksort(larger)

def partition(arr):
    if not arr:
        return [], [], []
    pivot = arr[0]
    smaller, equal, larger = [], [pivot], []
    for x in arr[1:]:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return smaller, equal, larger
