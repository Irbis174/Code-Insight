def linear_search_sentinel(arr, target):     last = arr[-1]     arr[-1] = target     i = 0     while arr[i] != target:         i += 1     arr[-1] = last     if i < len(arr) - 1 or last == target:         return i     return -1