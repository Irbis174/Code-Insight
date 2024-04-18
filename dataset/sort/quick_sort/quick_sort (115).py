def quicksort_with_insertion_sort(arr)
    if len(arr) = 10  # Threshold for switching to Insertion Sort
        for i in range(1, len(arr))
            key = arr[i]
            j = i - 1
            while j = 0 and arr[j]  key
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    else
        pivot = arr[len(arr)  2]
        left = [x for x in arr if x  pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x  pivot]
        return quicksort_with_insertion_sort(left) + middle + quicksort_with_insertion_sort(right)
