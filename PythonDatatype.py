######################### Numeric Datatype #########################

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

########################## List Datatype ################################

# Creating List

a = [] # Empty List
b = [1, 2, 3, 4] # List with One datatype (int)
c = [1, "2", [3, 4,5], (45, "asd"), {"a": [1, 2, 3]}] # List with different datatype
print(f'a: {a} | b: {b} | c: {c}')

a.append(3); a.append("x"); a.append("x"); print(f'a: {a}') # Adding elements to list
print(f'Count of x in List "a": {a.count("x")}') # Finding frequency of an element
print(f'combine list a and b: {a+b}') # Combining two list with + operator

#Appending multiple element in a list using extend
a.append({'y': (9,7,6,'1')}) # a.extend({'y': (9,7,6,'1')})
a.extend((9,7,6,'1')) # a.append((9,7,6,'1'))
print(f'Appending multiple elements to List "a": {a}')

#Insert element to particular index
a.insert(0, 'A')
print(f'Inserting element to a List "a" using Index: {a}')

# Accessing Elements in List
print(f'Accessing First five elements of List "a": {a[:5]}')
print(f'Accessing Element with Negative Index of List "a": {a[-1]}')
print(f'Accessing Element with specific interval on List "a": {a[::3]}')
print(f'c: {c}')
print(f'Accessing a List inside a List: {c[2][1:]}')
print(f'Accessing a tuple inside a List: {c[3][1]}')
print(f'Accessing a Dict inside a List: {c[4]["a"]}')


#Reversing List
a.reverse()
print(f'Reversing the List a using reverse() : {a}')
print("Reversed a: ", a)
print(f'Reversing the List a using Index: {a[::-1]}') # With Negative index the list reverse

#Removing elements from list
print(f'Dropping Element with Negative Index of List "a": {a[:-1]}')
print(f'Dropping Element with specific interval on List "a": {a[::-3]}') # With Negative index the list reverse
print("Element popped out is:", a.pop()) # removing last element added to the list
a.remove("x")
print(f'Removing element x from List {a}') # removing particular element

# Clear all the elements of the list
a.clear(); b.clear(); c.clear()
print(f'Clearning List "a": {a}, "b": {b}, "c": {c}')
