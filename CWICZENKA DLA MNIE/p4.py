def f(d):
    cars_in = set()
    cars_out = set()
    for x in range(len(d)):
        if d[x][1] == "in":
            cars_in.add(d[x][0])
        else:
            cars_out.add(d[x][0])
    cars_in -= cars_out
    return sorted(list(cars_in))
 

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

# print(f(cars))
# Output: ["BA111","GX444","KR234"]
cars_in = set()
cars_out = set()
for x in range(len(cars)):
    if cars[x][1] == "in":
            cars_in.add(cars[x][0])
    else:
            cars_out.add(cars[x][0])
cars_in -= cars_out
print(sorted(list(cars_in)))
            