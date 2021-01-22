country = input().split(", ")
capital = input().split(", ")

final_format = [print(f' {i} -> {j}') for i, j in zip(country, capital)]
