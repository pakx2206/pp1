def f(dictonary,x,y):
    suma = 0
    for wartosci in dictonary.values():
        if isinstance(wartosci, list):
            for liczba in wartosci:
                if x <= liczba <= y:
                    suma += liczba

    return suma

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) )