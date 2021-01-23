name = input().split(", ")
command = input()

heroes = {}

while not command == "End":
    name, item, price = command.split("-")
    if not heroes.get(name):
        heroes[name] = {}

    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

    command = input()
print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum(price for item, price in inventory.items())}" for name, inventory in heroes.items()], sep="\n")




# def get_count_items(name, d):
#     return len([value for key, value in d.items ()if key.startswith ( name )])
#
#
# def get_sum_costs(name, d):
#     return sum([value for key, value in d.items ()if key.startswith ( name )])
#
#
# names= input().split(', ')
# d={}
# while True:
#     comand = input()
#     if comand == "End":
#         break
#     name, item,cost =comand.split('-')
#     dict_key = name+'@'+item
#     if dict_key not in d:
#         d[dict_key]=int(cost)
# for name in names:
#     print(f'{name} -> Items: {get_count_items(name, d)}, Cost: {get_sum_costs(name, d)}')
