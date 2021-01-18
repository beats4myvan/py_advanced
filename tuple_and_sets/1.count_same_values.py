numbers = input().split(" ")

occurances = {}

for i in numbers:
    if not i in occurances:
        occurances[i] = 1
    else:
        occurances[i] += 1

for x, y in occurances.items():
    x = float(x)
    print(f"{x} - {y} times ")
