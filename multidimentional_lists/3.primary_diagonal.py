square_matrix = int(input())

matrix = []
sum_row = 0
for _ in range(square_matrix):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)
for row in range(len(matrix)):
   sum_row += matrix[row][row]

print(sum_row)
