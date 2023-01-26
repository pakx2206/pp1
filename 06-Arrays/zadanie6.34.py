arr = [5, 4, 3, 2, 6, 5]
arr1 = [5, 4, 3, 2, 10]
arr2 = []*len(arr)
g = 0
for x in range(len(arr)):
    for y in range(len(arr1)):
        if arr1[y] == arr[x]:
            g = 1

if g==0:
    print("false")
else: 
    print("True")
