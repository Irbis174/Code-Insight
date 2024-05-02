def bubble_sort_decorator(func):
    def wrapper(unsorted_data):
        data_len = len(unsorted_data)
        for outer_idx in range(data_len):
            for inner_idx in range(data_len - outer_idx - 1):
                if unsorted_data[inner_idx] > unsorted_data[inner_idx + 1]:
                    unsorted_data[inner_idx], unsorted_data[inner_idx + 1] = unsorted_data[inner_idx + 1], unsorted_data[inner_idx]
        return func(unsorted_data)
    return wrapper

@bubble_sort_decorator
def my_function(sorted_data):
    return sorted_data
