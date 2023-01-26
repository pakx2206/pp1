arr = [[1,2,3,4,5],[0,0,0,0,0],[6,7,8,9,0]] 
for x in range(3):
    arr[x][0], arr[x][-1] = arr[x][-1], arr[x][0]

for row in arr:
    print(*row)
