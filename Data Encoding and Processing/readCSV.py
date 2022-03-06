import csv

#Each column is read based on indexing
with open('dummy.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    #Iterate over records
    for row in f_csv:
        print(row[0])


#Each column is read based on column name
with open('dummy.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Symbol'])