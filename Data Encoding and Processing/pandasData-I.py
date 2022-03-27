import pandas as pd

stocks = pd.read_csv('dummy.csv')

#Filter Data
aig = stocks[stocks["Symbol"]=="AIG"]
print(f'Filtered Record: {aig}')

#groupby
date_groupby = stocks.groupby('Date')
date_counts = date_groupby.size()
print(f'Groupby Operation: {date_counts}')

"""
Filtered Record:   Symbol  Price       Date    Time  Change  Volume
1    AIG  71.38  6/12/2007  9:36am   -0.15  195500
Groupby Operation: Date
6/11/2007    3
6/12/2007    3
dtype: int64
"""