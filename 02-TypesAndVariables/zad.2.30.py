import random 
x = random.randint(1,6)
print(f'Dice rolled: {x}\nSpecial number: {x==1 or x==6}')