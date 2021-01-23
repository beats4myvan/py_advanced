numbers = input().split("|")
numbers.reverse()

result = [value for i in range(len(numbers)) for value in numbers[i].split()]

print(*result)
# result = [value.strip() for i in range(len(numbers)) for value in numbers[i].split()]
# print(*result)