import csv
with open('07-FileHandling/students.txt', 'r') as fcsv:
    writer = csv.DictReader(fcsv)
    for row in writer:
        if int(row['age']) < 30:
            print(row['first_name'],row['last_name'],row['email'])