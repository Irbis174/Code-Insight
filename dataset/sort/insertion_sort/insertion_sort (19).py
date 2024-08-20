def insertion_sort(collection):
    for index in range(1, len(collection)):
        current_item = collection[index]
        position = index - 1
        while position >= 0 and collection[position] > current_item:
            collection[position + 1] = collection[position]
            position -= 1
        collection[position + 1] = current_item
    return collection
