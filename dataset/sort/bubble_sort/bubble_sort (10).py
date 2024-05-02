def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range(0, length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst