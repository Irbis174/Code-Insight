def bubble_sort_algorithm(a, reverse=False):
    a_length = len(a)
    for i in range(a_length):
        swap_occurred = False
        for j in range(0, a_length - i - 1):
            if (a[j] > a[j + 1] and not reverse) or (a[j] < a[j + 1] and reverse):
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_occurred = True
        if not swap_occurred:
            break
    return a
