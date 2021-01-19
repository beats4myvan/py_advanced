rows, columns = list(map(int, input().split(", ")))

sum_el = 0

matrix = []

for i in range(rows):
    m_el = map(int, input().split(", "))
    matrix_1 = []
    for y in m_el:
        sum_el += y
        matrix_1.append(y)
    matrix.append(matrix_1)

print(sum_el)
print(matrix)
