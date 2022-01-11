# Assigning Names to Sequential elements instead using position/index
from collections import namedtuple

subscriber = namedtuple('Subscriber', ['mail', 'date'])
sub = subscriber('aaa@xyx.com', '2021-09-09')
print(sub.mail)

# Why namedtuples over indexed based retrivel
def compute_cost_position(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost_namedtuple(records):
    total = 0.0
    for rec in records:
        s = stock(*rec)
        total += s.shares * s.price
    return total

print(f"Total Amt in Stock Market: {compute_cost_namedtuple([('APL', 10, 320), ('PL', 120, 20)])}")

# Update namedtuple elements, namedtuple is immutable, 
# thus requires replace and assign to new namedtuple

s = stock('HP', 32, 100)
s = s._replace(shares = 45)
print(s.shares)