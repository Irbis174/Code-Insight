def quickselect(arr, k, left=0, right=None):     if right is None:         right = len(arr) - 1      pivot_index = random.randint(left, right)     left_pivot_index, right_pivot_index = partition(arr, left, right, pivot_index)      if k < left_pivot_index:         return quickselect(arr, k, left, left_pivot_index - 1)     elif k > right_pivot_index:         return quickselect(arr, k, right_pivot_index + 1, right)     else:         return arr[k]  def partition(arr, left, right, pivot_index):     pivot_value = arr[pivot_index]     arr[pivot_index], arr[right] = arr[right], arr[pivot_index]     left_pivot_index = left     right_pivot_index = right - 1      for i in range(left, right):         if arr[i] < pivot_value:             arr[i], arr[left_pivot_index] = arr[left_pivot_index], arr[i]             left_pivot_index += 1         elif arr[i] > pivot_value:             arr[i], arr[right_pivot_index] = arr[right_pivot_index], arr[i]             right_pivot_index -= 1             i -= 1      arr[right], arr[right_pivot_index + 1] = arr[right_pivot_index + 1], arr[right]     return left_pivot_index, right_pivot_index + 1