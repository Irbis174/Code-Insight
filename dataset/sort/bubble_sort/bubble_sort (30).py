def bubble_sort(data):
    arr_len = len(data)
    for i in range(arr_len):
        data[:arr_len-i] = sorted(data[:arr_len-i], reverse=True)[:arr_len-i-1] + data[arr_len-i:arr_len]
    return data
