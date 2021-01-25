n_usernames = int(input())
unique_names = []

for _ in range(n_usernames):
    name = input()
    if not name  in unique_names:
        unique_names.append(name)
print(*unique_names, sep='\n')
