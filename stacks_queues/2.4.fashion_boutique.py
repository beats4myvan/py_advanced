clothes = list(map(int, input().split(" ")))
rack_capacity = int(input())

needet_racks = 0
sum_rack = 0
while len(clothes) > 0:
    if sum_rack + clothes[-1] == rack_capacity:
        clothes.pop()
        needet_racks += 1
        sum_rack = 0
    elif sum_rack + clothes[-1] > rack_capacity:
        sum_rack = 0
        needet_racks += 1
    else:
        sum_rack += clothes.pop()
if not sum_rack == 0:
    needet_racks += 1
print(needet_racks)
