pin_code = "0805"
for x in range(3,0,-1):
    y = str(input("Enter the pin code:"))
    if y != pin_code:
        print("Incorrect...")
    if x==1:
        print("Sorry, your card has been blocked.")
    if y==pin_code:
        print("Correct!!!")
        exit()