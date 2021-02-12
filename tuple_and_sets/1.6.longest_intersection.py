number_n = int(input())
biggeset_intersection = []

for i in range(number_n):
    range_a, range_b = input().split("-")
    y = list(map(int, range_a.split(",")))
    x = list(map(int, range_b.split(",")))
    y_len = [x for x in range(y[0], y[1] + 1)]
    x_len = [x for x in range(x[0], x[1] + 1)]
    longeset = set(y_len).intersection(x_len)
    if len(longeset) > len(biggeset_intersection):
        biggeset_intersection = longeset

print(f'Longest intersection is {list(biggeset_intersection)} with length {len(biggeset_intersection)}')
