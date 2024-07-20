def quickselect(arr, k, left=0, right=None):     if right is None:         right = len(arr) - 1      if left == right:         return arr[left]      pivot_index = random.randint(left, right)     pivot_index = partition(arr, left, right, pivot_index)      if k == pivot_index:         return arr[k]     elif k < pivot_index:         return quickselect(arr, k, left, pivot_index - 1)     else:         return quickselect(arr, k, pivot_index + 1, right)  def partition(arr, left, right, pivot_index):     pivot_value = arr[pivot_index]     l = left     r = right      while True:         while arr[l] < pivot_value:             l += 1         while arr[r] > pivot_value:             r -= 1          if l >= r:             return l          arr[l], arr[r] = arr[r], arr[l]         l += 1         r -= 1