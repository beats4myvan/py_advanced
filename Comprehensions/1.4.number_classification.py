numbers = list(map(int, input().split(", ")))


def positive(nums):
    num = [str(i) for i in nums if i >= 0]
    final_nums = ', '.join(num)
    return print(f"Positive: {final_nums}")


def negative(nums):
    num = [str(i) for i in nums if i < 0]
    final_nums = ', '.join(num)
    return print(f"Negative: {final_nums}")


def even(nums):
    num = [str(i) for i in nums if i % 2 == 0]
    final_nums = ', '.join(num)
    return print(f"Even: {final_nums}")


def odd(nums):
    num = [(str(i)) for i in nums if i % 2 == 1]
    final_nums = ', '.join(num)
    return print(f"Odd: {final_nums}")


positive(numbers)
negative(numbers)
even(numbers)
odd(numbers)
