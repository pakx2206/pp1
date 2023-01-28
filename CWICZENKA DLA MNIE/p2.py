def f(arr):
    rows = len(arr)
    cols = len(arr[0])
    if rows!=cols:
        return False
    for x in range(1,rows+1):
        for y in range(1,cols+1):
            if arr[x-1][y-1]!=x*y:
                return False
    return True

print(f([[1,2,3],[2,4,6],[3,6,9]]))
