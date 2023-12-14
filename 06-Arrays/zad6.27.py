def difference(array):
    array.sort()
    return array[-1]-array[0]


print(difference([5,1,9,6,1]))