from collections import deque

quantity_of_food = int(input())
q_of_order = deque(map(int, input().split()))
print(max(q_of_order))

if not q_of_order:
    print(f'Orders complete')
else:
    print(f'Orders left: {" ".join(map(str, q_of_order))}')
while q_of_order and q_of_order[0] <= quantity_of_food:
    quantity_of_food -= q_of_order.popleft()

if not q_of_order:
    print(f'Orders complete')
else:
    print(f'Orders left: {" ".join(map(str, q_of_order))}')