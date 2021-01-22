word = input().split(" ")

even_lenght = [x for x in word if len(x) % 2 == 0]

print(*even_lenght, sep=" \n")
