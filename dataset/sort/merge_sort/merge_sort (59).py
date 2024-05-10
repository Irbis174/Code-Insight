def merge_sort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        merge_sort(left)
        merge_sort(right)
	l=r=k=0
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                lst[k]=left[l]
                l+=1
            else:
                lst[k]=right[r]
                r+=1
            k+=1
        while l<len(left):
            lst[k]=left[l]
            l+=1
            k+=1
        while r<len(right):
            lst[k]=right[r]
            r+=1
            k+=1
