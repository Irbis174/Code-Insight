def linear_search_frequency(arr, target):     freq = {}     for i in range(len(arr)):         freq[arr[i]] = freq.get(arr[i], 0) + 1         if arr[i] == target:             return i, freq[target]     return -1, freq.get(target, 0)