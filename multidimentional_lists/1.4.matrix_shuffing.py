row, col = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(row)]

command = input()

while not command == "END":
    command = command.split()
    if len(command) == 5 and command[0] == "swap":
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if row1 >= row and row2 >= row and col1 >= col and col2 >= col:
            print(f"Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print('\n'.join(' '.join(map(str, el)) for el in matrix))
    else:
        print(f'Invalid input!')

    command = input()
