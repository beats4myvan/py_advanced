def stronger_nums(nums):
    negative = sum(filter(lambda x: x < 0, nums))
    positive = sum(filter(lambda x: x > 0, nums))

    print(negative, positive, sep="\n")
    if abs(negative) > positive:
        print(f'The negatives are stronger than the positives')
    else:
        print(f'The positives are stronger than the negatives')


nums = list(map(int, input().split(" ")))
stronger_nums(nums)
