num_names = int(input())

unique_names = []
for _ in range(num_names):
    name = input()
    if not name in unique_names:
        unique_names.append(name)
    else:
        pass
for i in unique_names:
    print(i)
