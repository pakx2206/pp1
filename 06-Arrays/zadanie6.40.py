arr = [[-38,19],[5,40],[-7,11],[29,16]]
max = -float("inf")
min = +float("inf")
maxind = [0]*2
minind = [0]*2
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y]>max:
            max = arr[x][y]
            maxind = [x+1,y+1]
        if arr[x][y]<min:
            min = arr[x][y]
            minind = [x+1,y+1]

print(max,min,maxind,minind)
