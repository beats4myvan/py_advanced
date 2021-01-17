sequence = input()
is_balanced = True
characters = {"{": "}", "[": "]", "(": ")"}

opening_chars = []

for i in sequence:
    if i in "{[(":
        opening_chars.append(i)
    else:
        if not opening_chars:
            is_balanced = False
            break
        current_opening = opening_chars.pop()
        if not characters[current_opening] == i:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")