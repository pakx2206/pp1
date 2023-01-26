arr = [15, 8, 31, 47, 2, 19]
z = 0
for x in range(0,(len(arr)-1)):
    for y in range(0,(len(arr))-x-1):
        if arr[y] > arr[y+1]:
            z = arr[y]
            arr[y] = arr[y+1]
            arr[y+1] = z
            y=+1
        

print(arr)
