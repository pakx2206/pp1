import math
x = 182
inches = x/2.54
feet = int(inches//12)
inches = round(inches - feet*12,2)
print(inches,feet)
print(f'I am {x}cm tall, i.e. {feet} feet and {inches} inches')