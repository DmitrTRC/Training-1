for i in range(1, 8, 2):
    for j in range(i):
        print('"', end='') if j % 2 else print("'", end='')
    print()
