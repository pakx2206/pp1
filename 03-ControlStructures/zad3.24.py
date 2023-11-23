a = float(input("Current product price: "))
b = float(input("Previous product price: "))
if b*0.9>= a:
    print("Buy the product!")
    print(f'Product price reduced by {(1-(a/b))*100:.2f}%')