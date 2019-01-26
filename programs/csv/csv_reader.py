import csv

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print("{name} works in the {branch} department, and was born in {bday}".format(name=row[0], branch=row[1], bday=row[2]))

# https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python