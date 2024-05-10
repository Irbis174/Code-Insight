def list_generator_insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        j = i
        while j > 0 and lst[j - 1] > current_value:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = current_value
        yield lst
