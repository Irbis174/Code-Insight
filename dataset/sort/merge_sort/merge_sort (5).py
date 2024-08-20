def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle_index = len(unsorted_list) // 2
    left_sublist = unsorted_list[:middle_index]
    right_sublist = unsorted_list[middle_index:]

    sorted_left = merge_sort(left_sublist)
    sorted_right = merge_sort(right_sublist)

    return merge_sorted_sublists(sorted_left, sorted_right)

def merge(left_sublist, right_sublist):
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left_sublist) and right_index < len(right_sublist):
        if left_sublist[left_index] <= right_sublist[right_index]:
            merged_list.append(left_sublist[left_index])
            left_index += 1
        else:
            merged_list.append(right_sublist[right_index])
            right_index += 1

    merged_list.extend(left_sublist[left_index:])
    merged_list.extend(right_sublist[right_index:])

    return merged_list