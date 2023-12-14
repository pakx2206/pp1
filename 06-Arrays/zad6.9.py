arr = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
i = 0
slowo = ""
for word in arr:
    if len(word)>i:
        i=len(word)
        slowo = word

print(slowo)