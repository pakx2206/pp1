arr = [[3, 9, 2],[2, 4, 5],[7, 1, 6],[0, 4, 8]]
suma = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] % 2 == 0:
            suma += arr[x][y]

print(suma)
