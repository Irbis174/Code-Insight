def sort_merge(arr):
    if len(arr) <= 1:
        return

    middle = len(arr) // 2
    first_part = arr[:middle]
    second_part = arr[middle:]

    sort_merge(first_part)
    sort_merge(second_part)

    merge_inplace(arr, first_part, second_part)

def merge_inplace(arr, part1, part2):
    i, j, k = 0, 0, 0

    while i < len(part1) and j < len(part2):
        if part1[i] <= part2[j]:
            arr[k] = part1[i]
            i += 1
        else:
            arr[k] = part2[j]
            j += 1
        k += 1

    while i < len(part1):
        arr[k] = part1[i]
        i += 1
        k += 1

    while j < len(part2):
        arr[k] = part2[j]
        j += 1
        k += 1