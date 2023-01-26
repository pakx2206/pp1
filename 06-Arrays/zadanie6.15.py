arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        if y == x:
            arr[x][y] = 1
        print(arr[x][y], end=" ")
    print("\n")
