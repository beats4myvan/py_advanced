rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

first_diag = []
second_diag = []
col = -1
for i in range(rows):
    first_diag.append(matrix[i][i])
    col += 1
for j in range(rows):
    second_diag.append(matrix[j][col])
    col -= 1

first_diag_str = ', '.join([str(i) for i in first_diag])
second_diag_str = ', '.join([str(i) for i in second_diag])
print(f"First diagonal: {first_diag_str}. Sum: {sum(first_diag)}")
print(f"Second diagonal: {second_diag_str}. Sum: {sum(second_diag)}")
