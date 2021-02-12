def best_list_pureness(numbers, index):
    highest_pureness = 0
    rotations = 0
    for i in range(index + 1):
        pureless_numbers = [(x * numbers.index(x)) for x in numbers]
        sum_pureness_numbers = sum(pureless_numbers)
        numbers.insert(0, numbers.pop())
        if sum_pureness_numbers > highest_pureness:
            highest_pureness = sum_pureness_numbers
            rotations = i
    return f"Best pureness {highest_pureness} after {rotations} rotations"


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
