import random
def compVsPlayer(x):
    if(x==random.randrange(1,6)):
        return True
    else:
        return False

print(compVsPlayer(3))