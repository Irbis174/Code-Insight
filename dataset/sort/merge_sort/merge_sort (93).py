def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    mid = len(list_to_sort) // 2
    left = list_to_sort[:mid]
    right = list_to_sort[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left_list, right_list):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left_list) and right_idx < len(right_list):
        if left_list[left_idx] <= right_list[right_idx]:
            result.append(left_list[left_idx])
            left_idx += 1
        else:
            result.append(right_list[right_idx])
            right_idx += 1
    result += left_list[left_idx:]
    result += right_list[right_idx:]
    return result