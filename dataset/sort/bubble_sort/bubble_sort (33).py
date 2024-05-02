def bubble_sort(collection):
    coll_len = len(collection)
    for i in range(coll_len):
        collection = [y if x > y else x for x, y in zip(collection, collection[1:] + [collection[0]])]
    return collection
