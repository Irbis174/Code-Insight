def merge_sort(unsorted_sequence):
    if len(unsorted_sequence) <= 1:
        return unsorted_sequence

    middle_index = len(unsorted_sequence) // 2
    left_sublist = unsorted_sequence[:middle_index]
    right_sublist = unsorted_sequence[middle_index:]

    sorted_left = merge_sort(left_sublist)
    sorted_right = merge_sort(right_sublist)

    return merge_sorted_sublists(sorted_left, sorted_right)

def merge_sorted_sublists(left_part, right_part):
    merged_sequence = []
    left_index, right_index = 0, 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            merged_sequence.append(left_part[left_index])
            left_index += 1
        else:
            merged_sequence.append(right_part[right_index])
            right_index += 1

    merged_sequence.extend(left_part[left_index:])
    merged_sequence.extend(right_part[right_index:])

    return merged_sequence