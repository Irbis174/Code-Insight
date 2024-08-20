def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle_index = len(unsorted_list) // 2
    left_sublist = unsorted_list[:middle_index]
    right_sublist = unsorted_list[middle_index:]

    sorted_left = merge_sort(left_sublist)
    sorted_right = merge_sort(right_sublist)

    return merge_sorted_sublists(sorted_left, sorted_right)

def merge_sorted_sublists(left_part, right_part):
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            merged_list.append(left_part[left_index])
            left_index += 1
        else:
            merged_list.append(right_part[right_index])
            right_index += 1

    merged_list.extend(left_part[left_index:])
    merged_list.extend(right_part[right_index:])

    return merged_list