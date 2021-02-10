text = input()
unique_set = set()

for x in text:
    if x not in unique_set:
        unique_set.add(x)
final_result = sorted(unique_set)
for x in final_result:
    print(f'{x}: {text.count(x)} time/s')