import csv

readCSV = csv.reader("~/code/git-history-data/githist.csv", delimiter=',')

counter = 0
for row in readCSV:
    print(row)
    counter += 1
    if counter == 20: exit