text = "Hello World"
print(f'Left Adjust: {text.ljust(20)}')
print(f'Right Adjust: {text.rjust(20)}')
print(f'Centering: {text.center(20)}')

print(f'Left Adjust: {text.ljust(15, "-")}')
print(f'Right Adjust: {text.rjust(15, "+")}')
print(f'Centering: {text.center(15, "*")}')

#Alternative Way
print(f' {format(text, ">20")}') #->20s
print(f' {format(text, "<20")}') #+>20s
print(f' {format(text, "^20")}')