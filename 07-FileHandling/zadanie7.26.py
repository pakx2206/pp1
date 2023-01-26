import re
with open('07-FileHandling/tekst.txt', 'r') as f:
    xd = f.read()
    sum = re.findall(r'\b\w{6,}\b', xd)
    for word in sum:
        print(word)
