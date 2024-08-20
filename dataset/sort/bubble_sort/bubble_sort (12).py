def bubble_sort(lst):
    length = len(lst)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(length - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                
    return lst