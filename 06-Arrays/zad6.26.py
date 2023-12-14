def second_largest(array):
    array.sort()
    return array[-2]


print(second_largest([5,1,9,6,1]))