def convert(m):
    arr = [0]*len(m)*len(m[0])
    for x in range(len(m)):
        for y in range(len(m[x])):
            arr[x*len(m[x])+y] = m[x][y]
    return arr

x = convert([[1,2,3,4,5], [6,7,8,9,0]])

print(x)



