def merge_sort(arr):
    if len(arr) <= 1:
        return

    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    merge_sort(l)
    merge_sort(r)

    merge_in_place(arr, l, r)

def merge_in_place(arr, l, r):
    i, j, k = 0, 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1