def bubble_sort(lst):
    length = len(lst)
    
    for i in range(length):
        for j, value in enumerate(lst[:length - i]):
            if value > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], value
                
    return lst