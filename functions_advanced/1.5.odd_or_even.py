def even_odd(command, nums):
    even = sum(filter(lambda x: x % 2 == 0, nums))
    odd = sum(filter(lambda x: x % 2 == 1, nums))
    if command == 'Odd':
        return odd * len(nums)
    else:
        return even * len(nums)


command = input()
nums = list(map(int, input().split(" ")))
print(even_odd(command, (nums)))
