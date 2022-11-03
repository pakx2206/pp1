import math
print("Enter the amount in PLN:", end=" ")
suma=int(input())
print(f"The amount of PLN {suma} in coins:")
print("5 zł -", math.floor(suma/5))
suma=suma%5
print("2 zł -", math.floor(suma/2))
suma=suma%2
print("1 zł -", suma)