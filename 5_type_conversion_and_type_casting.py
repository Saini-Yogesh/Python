a = 2
b = 5.9
c = "4"

print(a+b) # type conversion to the next superior data type
# print(a+c) # will give error -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+int(c)) # type casting

# type casting is possibe if the number to string and string to number(only numbres)
z = str(648)
print(type(z)) # will give str