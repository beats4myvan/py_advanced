numbers = input().split()

s = []
for el in numbers:
    s.append(el)

result = []

while s:
    result.append(s.pop())

print(' '.join(result))
