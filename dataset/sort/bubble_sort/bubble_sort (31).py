def bubble_sort(container):
    length = len(container)
    for i in range(length):
        if all(container[j] <= container[j+1] for j in range(length-i-1)):
            break
        for j in range(length-i-1):
            if container[j] > container[j+1]:
                container[j], container[j+1] = container[j+1], container[j]
    return container
