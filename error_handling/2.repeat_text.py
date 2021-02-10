try:
    text = input()
    times = int(input())

    word =text * times
    print(word)
except ValueError:
    print('Variable times must be an integer')