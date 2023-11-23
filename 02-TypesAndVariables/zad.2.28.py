height = float(input("Enter your height in cm: "))/100
weight = float(input("Enter your weight in kg: "))
print(f'Your BMI index: {round(weight/(height*height),1)}')
print(f'Correct weight: {round(weight/(height*height),1)>18.5 and round(weight/(height*height),1)<25.0 }')