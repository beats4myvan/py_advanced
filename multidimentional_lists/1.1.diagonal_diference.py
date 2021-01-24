square_matrix = int(input())

matrix = []
sum_primary = 0
sum_secondary = 0
cur_col = len(matrix) - 1

# cur_col = -1
# for _ in range(square_matrix):
#     row = [int(x) for x in input().split(' ')]
#     matrix.append(row)
matrix = [[int(x) for x in input().split(' ')] for _ in range(square_matrix)]

for row in range(len(matrix)):
    sum_primary += matrix[row][row]
    sum_secondary += matrix[row][cur_col]
    cur_col -= 1

print(abs(sum_primary - sum_secondary))
