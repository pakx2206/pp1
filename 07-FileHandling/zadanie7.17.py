org = '07-FileHandling/text.txt'
copy = '07-FileHandling/copycopy.txt'
with open(org,'r') as orginal:
    with open(copy,'w') as copy:
        for line in orginal:
            copy.write(line)

print(copy)