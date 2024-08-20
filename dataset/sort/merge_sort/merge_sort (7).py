def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    left, right = split_list(lst)

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge_lists(sorted_left, sorted_right)

def split_list(lst):
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return left, right

def merge_lists(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged