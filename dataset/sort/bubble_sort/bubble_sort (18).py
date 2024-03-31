def bubble_sort_custom_key(arr, comparison_key=lambda x: x):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if comparison_key(arr[j]) > comparison_key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr