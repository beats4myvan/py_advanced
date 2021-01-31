def ascending_nums(nums):
    return sorted(nums)


nums = map(int, input().split(" "))
print(ascending_nums(nums))