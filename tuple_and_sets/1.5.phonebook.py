phoneBook = {}

while True:
    name_and_number = input()
    if name_and_number.isdigit():
        search_num = int(name_and_number)
        break
    else:
        name, number = name_and_number.split("-")
        phoneBook[name] = number

for i in range(search_num):
    search_name = input()
    if search_name in phoneBook:
        print(f'{search_name} -> {phoneBook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')
