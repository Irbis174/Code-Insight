def insertion_sort(data, length):
    if length <= 1:
        return

    insertion_sort(data, length - 1)

    last_value = data[length - 1]
    position = length - 2

    while position >= 0 and data[position] > last_value:
        data[position + 1] = data[position]
        position -= 1

    data[position + 1] = last_value
    return data
