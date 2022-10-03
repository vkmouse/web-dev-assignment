from functions import *
import csv

filename = 'data.csv'
minYear = 2015
acceptableRegions = ['中正區', '萬華區', '中山區', '大同區', '大安區',
                     '松山區', '信義區', '士林區', '文山區', '北投區',
                     '內湖區', '南港區']

results = getResults()
results = filter(lambda result: checkPostDateAfterSpecificYear(result['xpostDate'], minYear), results)
rows = map(lambda result: convertResultToRow(result), results)
rows = filter(lambda row: checkRegionInAcceptableRegions(row[1], acceptableRegions), rows)

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)