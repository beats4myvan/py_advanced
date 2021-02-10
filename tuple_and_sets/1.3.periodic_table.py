n_lines = int(input())

unique_ones = []
for _ in range(n_lines):
    chemical_compounds = input().split(" ")
    for i in chemical_compounds:
        if i not in unique_ones:
            unique_ones.append(i)

for i in unique_ones:
    print(i)
