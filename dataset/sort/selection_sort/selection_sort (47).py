def GeneratorSelectionSort(data_container):
    for curr_idx in range(len(data_container)):
        min_idx = min((j for j in range(curr_idx, len(data_container))), key=lambda j: data_container[j])
        data_container[curr_idx], data_container[min_idx] = data_container[min_idx], data_container[curr_idx]
    return data_container