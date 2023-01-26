arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for x in range(0,5):
    for y in range(0,5):
        arr[x][y]+=(x+1)*(y+1)
        

for row in arr:
    print(*row)