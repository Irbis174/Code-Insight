def merge(left, right):
    merged=[]
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            merged.append(left[l])
            l+=1
        else:
            merged.append(right[r])
            r+=1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)