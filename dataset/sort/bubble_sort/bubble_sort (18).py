def bubble_sort(lst):
    length = len(lst)
    
    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]
        
    for i in range(length):
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                swap(j, j + 1)
                
    return lst