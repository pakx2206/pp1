arr = [[1, 2, 3, 4],[5, 6, 7, 8]]
for x in range(0,2):
    for y in range(0,4):
        if y == 3:
            print(arr[x][y], end="\n")
        else:
            print(arr[x][y], end="")
    