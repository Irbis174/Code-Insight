def bubble_sort(lst):
    length = len(lst)
    
    def sort(i):
        if i == length:
            return
        
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        
        sort(i + 1)
        
    sort(1)
    return lst