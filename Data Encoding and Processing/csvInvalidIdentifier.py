from collections import namedtuple
import re
import csv
from collections import namedtuple

# Company Symbol,Trade-Price,Date,Time,Change,Volume
# AA,39.48,6/11/2007,9:36am,-0.18,181800

with open('stock.csv') as f:
    f_csv = csv.reader(f)
    header = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', header)
    for r in f_csv:
        row = Row(*r)
        print(row)
        break

# Company_Symbol,Trade_Price,Date,Time,Change,Volume