import random
def rand_elem(array):
    return array[random.randrange(0,len(array))]

print(rand_elem([4,2,8,4,7,9,5]))