rows, cols = [int(i) for i in input().split(" ")]

matrix = []

word = input()

for row_index in range(rows):
    matrix.append([0 for el in range(cols)])
index_word = 0

for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index][col_index] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0

for rowIndex in range(rows):
    if rowIndex % 2 == 1:
        matrix[rowIndex].reverse()
    print(''.join(matrix[rowIndex]))