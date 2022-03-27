import pandas as pd

stocks = pd.read_csv("dummy.csv")

#count by value
stocks_cv = stocks['Date'].value_counts()
print(f'Value Count: {stocks_cv}')

#Filter based on Condition
stock_price = stocks[stocks['Price']>50]
print(f'Stocks greater than 50: {stock_price}')

"""
Value Count: 6/11/2007    3
6/12/2007    3
Name: Date, dtype: int64
Stocks less than 50:   Symbol  Price       Date    Time  Change  Volume
1    AIG  71.38  6/12/2007  9:36am   -0.15  195500
2    AXP  62.58  6/12/2007  9:36am   -0.46  935000
3     BA  98.31  6/11/2007  9:36am    0.12  104800
"""