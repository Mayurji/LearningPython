# Numeric Datatype

#type function to find numeric datatype
print(type(5.0))
print(type(3))
print(type(3+4j))

#Type Casting

print(type(int(5.0)))
print(type(complex(5.0)))

#Conversion based on precedence

print(type(1+2.0)) # Float has higher precedence than Int
print(type(5.0 + (3+ 4j))) # Complex has higher precedence than float

#Converting string numeric to numeric type
print(type(int('5')))
print(type(float('5.0')))
print(type(complex('4+3j')))
