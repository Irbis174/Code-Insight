def merge(left,right):
    result=[]
    left_idx=right_idx=0
    len_left,len_right=len(left),len(right)
    for _ in range(len_left+len_right):
        if left_idx<len_left and right_idx<len_right:
            if left[left_idx]<=right[right_idx]:
                result.append(left[left_idx])
                left_idx+=1
            else:
                result.append(right[right_idx])
                right_idx+=1
        elif left_idx<len_left:
            result.append(left[left_idx])
            left_idx+=1
        elif right_idx<len_right:
            result.append(right[right_idx])
            right_idx+=1
    return result

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)