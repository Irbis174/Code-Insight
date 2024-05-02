from collections import deque

def quicksort(unsorted_list):
    stack = deque([(0, len(unsorted_list) - 1)])
    while stack:
        left_index, right_index = stack.pop()
        if left_index >= right_index:
            continue
        pivot_value = unsorted_list[right_index]
        pivot_index = left_index - 1
        for j in range(left_index, right_index):
            if unsorted_list[j] <= pivot_value:
                pivot_index += 1
                unsorted_list[pivot_index], unsorted_list[j] = unsorted_list[j], unsorted_list[pivot_index]
        unsorted_list[pivot_index + 1], unsorted_list[right_index] = unsorted_list[right_index], unsorted_list[pivot_index + 1]
        stack.append((left_index, pivot_index - 1))
        stack.append((pivot_index + 2, right_index))
