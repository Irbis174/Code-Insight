def insertion_sort(arr):
    result = []
    for i in range(1, len(arr)):
        new_arr = arr[:i]
        new_arr.append(arr[i])
        new_arr = sorted(new_arr)
        result = new_arr + arr[i+1:]
    return result
