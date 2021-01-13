text = input()

stack = []

for i in range(len(text)):
    ch = text[i]
    if ch == "(":
        stack.append(i)
    elif ch == ")":
        x = stack.pop()
        print(text[x:i+1])