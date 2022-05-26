import json
import csv

with open ('./data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = {'names': []}
    for row in reader:
        data['names'].append({'InvoiceNo': row[0], 'StockCode': row[1],'Description': row[2],'Quantity': row[3],
                             'InvoiceDate': row[4],'UnitPrice': row[5],'CustomerID': row[6],'Country': row[7]})
