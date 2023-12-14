arr = [[2,5,4],[9,0,3]]

print(arr)
print(len(arr),len(arr[0]))
print(arr[1][1])
print(arr[0][2])
for x in arr[1]:
    print(x,end = " ")
print("\n")
for x in range(0,2):
    for y in range(0,3):
        if y<2:
            print(arr[x][y],end = " ")
        elif y==2:
            print(arr[x][y],end = "\n")

print(arr[0][-1],end="\n")
print(arr[1][-1],end="\n")