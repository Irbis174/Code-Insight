def bubble_sort(list1):
    # We can stop the iteration once the swap has done
    has_swapped = True

    while (has_swapped):
        has_swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                # Swap
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
    return list1
