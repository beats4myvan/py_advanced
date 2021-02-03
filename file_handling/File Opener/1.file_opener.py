try:
    with open('text.txt', 'r') as f:
        print(f"File found")
        print(f.read())
        # print(f.read(46))
except FileNotFoundError:
    print(f"File not found")

