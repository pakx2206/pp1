def read_number():
    suma = 0
    print("Enter the number:")
    x=int(input())
    suma = suma + x
    print("Enter the number:")
    y=int(input())
    suma = suma + y
    return suma


print(read_number())
