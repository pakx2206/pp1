def identity_matrix(n):
    arr = [[0]*n for _ in range(n)]
    for x in range(n):
        arr[x][x]+=1
    return arr

print(identity_matrix(3))