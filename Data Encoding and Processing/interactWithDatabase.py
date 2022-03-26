import sqlite3

stocks = [
('GOOG', 100, 490.1),
('AAPL', 50, 545.75),
('FB', 150, 7.45),
('HPQ', 75, 33.2),
]

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE PORTFOLIO (Symbol TEXT, Share INTEGER, Price REAL)")
cursor.executemany("INSERT INTO PORTFOLIO VALUES (?,?,?)", stocks)
db.commit()