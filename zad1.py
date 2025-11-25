def sum_list(nums):
    total = 0
    for x in nums:
        total += x
    return total

def sum_list_rec(nums):
    if not nums:
        return 0
    return nums[0] + sum_list_rec(nums[1:])

nums = [5, 3, 10, 7, 2]
print(sum_list(nums))
print(sum_list_rec(nums))