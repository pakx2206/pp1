arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
for x in range(0,len(arr1)):
    for y in range(0,len(arr2)):
        if arr1[x]==arr2[y]:
            arr1[x]=0

for x in range(0,len(arr1)):
    if arr1[x]!=0:
        print(arr1[x], end = " ")
