# Function with no arguments
def dummy_function():
    return "Function with no arguments"

# Function with two arguments
def addition(arg1, arg2):
    return arg1 + arg2

# Function with undefined number of arguments
def summation(*args):
    num = 0
    for n in args:
        num += n
    return num

print(f'Dummy Function: {dummy_function()}')
print(f'Addition of two numbers: {addition(1, 2)}')
print(f'Summation of Numbers: {summation(1, 2, 3, 4, 5)}')