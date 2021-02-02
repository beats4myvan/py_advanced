def even_odd(*args):
    command = args[-1]
    nums = args[:-1]
    even = list(filter(lambda x: x % 2 == 0, nums))
    odd = list(filter(lambda x: x % 2 == 1, nums))
    if command == 'odd':
        return odd
    else:
        return even


# print(even_odd(1, 2, 3, 4, 5, 6,"even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))