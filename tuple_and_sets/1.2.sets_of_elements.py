n, m = [int(i) for i in input().split(" ")]

lenght_n = set([])
lenght_m = set([])

for i in range(n):
    lenght_n.add(input())
for _ in range(m):
    lenght_m.add(input())
print(*lenght_n.intersection(lenght_m), sep='\n')