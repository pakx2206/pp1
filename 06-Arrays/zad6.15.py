arr = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0,3):
        if x==y:
            arr[x][y]=1
for x in range(0,3):
    for y in range(0,3):
        if y<2:
            print(arr[x][y],end=" ")
        else:
            print(arr[x][y],end="\n")




print(arr)