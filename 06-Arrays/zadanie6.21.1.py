def compare(array1, array2):
    x = len(array1)
    z = len(array2)
    suma = 0
    if x == z:
        for y in range(0, x):
            if array1[y] == array2[y]:
                suma += 1
        if suma == x:
            return True
        else:
            return False
    else:
        return False


print(compare())
