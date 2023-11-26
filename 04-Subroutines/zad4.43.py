def f(name):
    s = ""
    name = name.split()
    for word in name:
        s += word[0]
    return s
print(f("Internet of Things"))