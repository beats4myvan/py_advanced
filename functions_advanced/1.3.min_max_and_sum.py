def sort(nums):
    return f"The minimum number is {min(nums)}\nThe maximum number is {max(nums)}\n" \
           f"The sum number is: {sum(nums)}"


nums = list(map(int, input().split(" ")))
print(sort(nums))