def BuiltInSelection_Sort(data_numbers):
    sorted_numbers = []
    for _ in range(len(data_numbers)):
        min_val = min(data_numbers)
        sorted_numbers.append(min_val)
        data_numbers.remove(min_val)
    return sorted_numbers