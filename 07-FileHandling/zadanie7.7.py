with open('07-FileHandling/countries.txt', 'r') as file:
    for line in file:
        print(line,end="")

    file.close()
