import csv
import json

# utf8 error in data
with open('./data.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({'InvoiceNo': row[0], 'StockCode': row[1], 'Description': row[2], 'Quantity': row[3],
                     'InvoiceDate': row[4], 'UnitPrice': row[5], 'CustomerID': row[6], 'Country': row[7]})


with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
