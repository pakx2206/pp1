def f(array2D):
    arr = [0]*len(array2D[0])
    for x in range(0,len(array2D)):
        for y in range(0,len(array2D[0])):
            arr[y] += array2D[x][y]
    return arr

print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )