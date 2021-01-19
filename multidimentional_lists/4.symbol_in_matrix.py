size = int(input())

# matrix_of_chars = [[] * size for x in range(0, size)]
matrix_of_chars = []
for x in range(0, size):
    matrix_of_chars.append(input())

symbol = input()
location = []
found = False

for row in range(0, size):
    if found:
        break
    for col in range(0, size):
        if matrix_of_chars[row][col] == symbol:
            location = [row, col]
            found = True

if found == True:

    print(f"({location[0]}, {location[1]})")

else:

    print(f"{symbol} does not occur in the matrix")
