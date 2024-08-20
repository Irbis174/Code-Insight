def bubble_sort(lst)
    length = len(lst)
    
    for i in range(length)
        lst = [lst[j + 1] if lst[j]  lst[j + 1] else lst[j] for j in range(length - i - 1)] + lst[length - i]
        
    return lst