arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]
arr3 = [0] * 100
z = 0
for x in range(0, 7):
    for y in range(0, 3):
        if arr1[x] == arr2[y]:
            arr3[z] = arr2[y]
            z += 1

while z != 0:
    print(arr3[z-1], end=" ")
    z-=1

