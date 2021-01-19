num_of_commands = int(input())

parking_lot = []

for _ in range(num_of_commands):
    direction, car_number = input().split(", ")
    if (direction == "IN") and (car_number not in parking_lot):
       parking_lot.append(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)
if parking_lot:
    for i in parking_lot:
        print(i)
else:
    print(f'Parking Lot is Empty')