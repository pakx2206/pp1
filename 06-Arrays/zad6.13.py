arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum=0
for x in range(0,4):
    for y in range(0,3):
        if arr[x][y]%2==0:
            sum+=arr[x][y]

print(sum)