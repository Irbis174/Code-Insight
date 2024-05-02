quicksort = lambda nums: quicksort([x for x in nums[1:] if x < nums[0]]) + \
                         [nums[0]] + \
                         quicksort([x for x in nums[1:] if x >= nums[0]]) if nums else []
