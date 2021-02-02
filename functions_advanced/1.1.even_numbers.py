def even_nums(nums):
    return  list(filter(lambda x: x % 2 == 0, nums))

    # only_even = [n for n in nums if n % 2 == 0]




nums = map(int, input().split(" "))
print(even_nums(nums))