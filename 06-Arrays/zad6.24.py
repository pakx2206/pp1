arr = [2,3,2,5,8,1,9,8]
arr1 = [0]*max(arr)
print(arr1)
for x in range(0,len(arr)):
    arr1[arr[x]-1]+=1

for x in range(0,len(arr1)):
    if arr1[x]==1:
        print(x+1, end = " ")

