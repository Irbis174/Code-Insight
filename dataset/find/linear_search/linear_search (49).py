def linear_search_min_max(arr, target):     min_val, max_val = min(arr), max(arr)     if target < min_val or target > max_val:         return -1     for i in range(len(arr)):         if arr[i] == target:             return i     return -1