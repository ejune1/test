# merge sort

nums = [1,4,5,3,6,7,8,3,4,0,9,8,7,5,4,3,4,5,6,7,8,9,1,2]
print(nums)

def merge_sort(nums):
    if (len(nums) == 0) or (len(nums) == 1):
        return nums

    #divide into two lists
    middle = len(nums) // 2
    left  = nums[:middle]
    right = nums[middle:]

    #recursively sort each list
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    #combine results into list
    res = []
    
    while (len(left_sorted) > 0) or (len(right_sorted) > 0):
        if len(left_sorted) == 0:
            res.append(right_sorted.pop(0))
        elif len(right_sorted) == 0:
            res.append(left_sorted.pop(0))
        elif left_sorted[0] <= right_sorted[0]:
            res.append(left_sorted.pop(0))
        else:
            res.append(right_sorted.pop(0))

    return res

res = merge_sort(nums)
print(res)
