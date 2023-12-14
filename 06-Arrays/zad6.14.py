arr = [[True,False],[True,True],[False,False]]

for x in range(0,3):
    for y in range(0,2):
        if arr[x][y]==True:
            arr[x][y]=False
        else:
            arr[x][y]=True

print(arr)