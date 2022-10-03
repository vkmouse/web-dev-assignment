from functions import *
import csv

filename = 'data.csv'
minYear = 2015

results = getResults()
results = filter(lambda result: checkPostDateAfterSpecificYear(result['xpostDate'], minYear), results)
rows = map(lambda result: convertResultToRow(result), results)

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)