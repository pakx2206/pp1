arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for x in range(0,5):
    for y in range(0,5):
        arr[x][y] = (x+1)*(y+1)

for x in range(len(arr)):
    for y in range(len(arr[0])):
        if y==len(arr[0])-1:
            print(arr[x][y], end = "\n")
        else:
            print(arr[x][y], end = " ")