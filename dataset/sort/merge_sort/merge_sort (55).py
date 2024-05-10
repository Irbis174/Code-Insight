def merge_sort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        merge_sort(left)
        merge_sort(right)
        l=r=0
        for i in range(len(lst)):
            if l<len(left) and r<len(right):
                if left[l]<right[r]:
                    lst[i]=left[l]
                    l+=1
                else:
                    lst[i]=right[r]
                    r+=1
            elif l<len(left):
                lst[i]=left[l]
                l+=1
            else:
                lst[i]=right[r]
                r+=1