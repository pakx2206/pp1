x = float(input("Enter price: "))
y = float(input("Enter discount %: "))/100
print(f'Price with discount: {x*(1-y):.02f}')
print(f'Reduction: {x*y:.02f}')