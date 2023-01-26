arr = [[True,False],[True,True],[False,False]]
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] == True:
            arr[x][y] = False
        else: arr[x][y] = True

print(arr)