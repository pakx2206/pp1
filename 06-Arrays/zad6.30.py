def minmax(array):
    array.sort()
    return f'Resutls: [{array[0]},{array[-1]}]'


print(minmax([4,2,8,4,7,9,5]))