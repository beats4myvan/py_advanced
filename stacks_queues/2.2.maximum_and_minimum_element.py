from collections import deque

n_queries = int(input())

stack = deque()

for i in range(n_queries):
    query = input()
    if query.startswith('1'):
        index, query = query.split()
        stack.appendleft(int(query))
    elif query == '2':
        if len(stack) > 0:
            stack.popleft()
    elif query == '3':
        if len(stack) == 0:
            pass
        else:
            print(max(stack))
    elif query == '4':
        if len(stack) == 0:
            pass
        else:
            print(min(stack))

stacks = list(map(lambda x: str(x), stack))

print(", ".join(stacks))