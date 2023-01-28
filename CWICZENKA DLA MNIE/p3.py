def f1(t):
    import re
    s = re.findall(r'\b(?:[A-Z][a-z]*|\d+)', t)
    ese = {}
    for x in range(0, len(s), 2):
        ese[s[x]] = int(s[x+1])
    return dict(sorted(ese.items()))


def f2(d):
    import re
    s = re.findall(r'\b\d+',d)
    y = 0
    for x in s:
        y += int(x)
    return y


print(f2("Mark is 24 and Ann is 27"))
