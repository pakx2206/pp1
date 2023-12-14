import random
def rand_elem(array):
    return array[random.randrange(0,len(array),1)]

print(rand_elem([2,3,45,5,6,7,8,9]))