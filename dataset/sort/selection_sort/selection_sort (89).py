def selection_sort(number_list):
    n = len(number_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if number_list[j] < number_list[min_idx]:
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
    return number_list
