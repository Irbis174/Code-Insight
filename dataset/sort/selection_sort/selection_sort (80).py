def selection_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if list_of_numbers[j] < list_of_numbers[min_idx]:
                min_idx = j
        list_of_numbers[i], list_of_numbers[min_idx] = list_of_numbers[min_idx], list_of_numbers[i]
    return list_of_numbers
