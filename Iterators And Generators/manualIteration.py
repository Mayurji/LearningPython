# Manually Running Through Iterator Using next()

with open('dummy.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass


with open('dummy.txt') as f:
    while True:
        line = next(f)
        if line is None:
            break
        print(line, end='')