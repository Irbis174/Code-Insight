def mergesort_proc(arr):
    if len(arr) <= 1:
        return

    mid_point = len(arr) // 2
    left_arr = arr[:mid_point]
    right_arr = arr[mid_point:]

    mergesort_proc(left_arr)
    mergesort_proc(right_arr)

    merge_inplace(arr, left_arr, right_arr)

def merge_inplace(target, left, right):
    l_idx, r_idx, t_idx = 0, 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            target[t_idx] = left[l_idx]
            l_idx += 1
        else:
            target[t_idx] = right[r_idx]
            r_idx += 1
        t_idx += 1

    while l_idx < len(left):
        target[t_idx] = left[l_idx]
        l_idx += 1
        t_idx += 1

    while r_idx < len(right):
        target[t_idx] = right[r_idx]
        r_idx += 1
        t_idx += 1