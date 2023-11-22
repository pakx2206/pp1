import math
import random
def dice():
    x = random.randrange(1,6)
    return (x==1 or x==6)

print(dice())