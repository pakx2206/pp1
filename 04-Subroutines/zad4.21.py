import mykeyboard
import mymath

x = mykeyboard.read_number()
y = mymath.generate_number()
print(f'Computer number: {y}')
if x==y:
    print("You won the game!")
else:
    print("You lose the game!")