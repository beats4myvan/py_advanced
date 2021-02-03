with open('numbers.txt', 'r') as nums:
    sums = 0
    for number in nums:
        sums += int(number)
    print(sums)
