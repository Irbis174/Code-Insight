def built_in_selection_sort(numbers):
    sorted_numbers = []
    for _ in range(len(numbers)):
        min_val = min(numbers)
        sorted_numbers.append(min_val)
        numbers.remove(min_val)
    return sorted_numbers