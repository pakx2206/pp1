arr = [[1,2,3,4,5],[0,0,0,0,0],[6,7,8,9,0]] 
arr[0],arr[-1] = arr[-1],arr[0]
for row in arr:
    print(*row)