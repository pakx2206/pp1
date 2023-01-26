def transpose_matrix(m):
    arr = [[0]*len(m) for _ in range(len(m[0]))]
    for x in range(len(m)):
        for y in range(len(m[x])):
            arr[y][x] = m[x][y]
    return arr



x = transpose_matrix([[1, 2, 3,4,5], [6,7,8,9,0]])

for row in x:
    print(*row)