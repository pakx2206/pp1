a = int(input("Dog's age: "))
sum = 0
if a == 1:
    print(f'10.5')
for x in range(0,a):
    if x<2:
        sum += 10.5
    else:
        sum += 4
print(f'wynik: {int(sum)}')