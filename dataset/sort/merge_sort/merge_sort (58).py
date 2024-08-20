def merge(left, right):
    result=[]
    left_idx=right_idx=0
    while left_idx<len(left) and right_idx<len(right):
        if left[left_idx]<=right[right_idx]:
            result.append(left[left_idx])
            left_idx+=1
        else:
            result.append(right[right_idx])
            right_idx+=1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)
