square_matrix = int(input())

matrix = []
sum_primary = 0
sum_secondary = 0
cur_row = -1
for _ in range(square_matrix):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)
for row in range(len(matrix)):
    sum_primary += matrix[row][row]
    cur_row += 1
for i in range(len(matrix)):
    sum_secondary += matrix[cur_row][i]
    cur_row -= 1

final = abs(sum_primary - sum_secondary)
print(final)