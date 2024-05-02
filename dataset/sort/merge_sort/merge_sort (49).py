def merge_sort(lst, start=0, end=None):
    if end is None:
        end = len(lst)

    if end - start <= 1:
        return lst[start:end]

    mid = (start + end) // 2
    left = merge_sort(lst, start, mid)
    right = merge_sort(lst, mid, end)

    return merge(left, right)
