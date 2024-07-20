def quickselect(arr, k, left=0, right=None):     if right is None:         right = len(arr) - 1      if left == right:         return arr[left]      pivot_index = random.randint(left, right)         pivot_index = partition(arr, left, right, pivot_index)      if k == pivot_index:         return arr[k]     elif k < pivot_index:         return quickselect(arr, k, left, pivot_index - 1)     else:         return quickselect(arr, k, pivot_index + 1, right)  def partition(arr, left, right, pivot_index):     pivot_value = arr[pivot_index]     arr[pivot_index], arr[right] = arr[right], arr[pivot_index]     store_index = left      for i in range(left, right):         if arr[i] <= pivot_value:             arr[i], arr[store_index] = arr[store_index], arr[i]             store_index += 1      arr[right], arr[store_index] = arr[store_index], arr[right]     return store_index