(row, col) = [int(x) for x in input().split()]

max_sum = -999999999
matrix_3x3 = []
matrix = [[int(x) for x in input().split()] for _ in range(row)]

for i in range(row - 2):
    for j in range(col - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
                      matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            matrix_3x3 = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                          [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                          [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]

print(f"Sum = {max_sum}")

print(' '.join(' '.join(map(str, el)) for el in matrix_3x3))
