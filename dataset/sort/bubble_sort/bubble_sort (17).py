def bubble_sort(lst):
    length = len(lst)
    swap = lambda i, j: (lst[j], lst[i]) if lst[i] > lst[j] else (lst[i], lst[j])
    
    for i in range(length):
        for j in range(length - i - 1):
            lst[j], lst[j + 1] = swap(j, j + 1)
            
    return lst