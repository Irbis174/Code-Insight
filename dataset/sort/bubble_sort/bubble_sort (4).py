def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1

