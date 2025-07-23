# Arithmetic Operators (+, -, *, /, %, **)
a = 10
b = 3

print("Addition (+):", a + b)        # 13
print("Subtraction (-):", a - b)     # 7
print("Multiplication (*):", a * b)  # 30
print("Division (/):", a / b)        # 3.333...
print("Modulus (%):", a % b)         # 1
print("Exponentiation (** or ^(in C++)):", a ** b) # 1000

# Relational / Comparison Operators (==, !=, >, <, >=, <=)
x = 5
y = 8

print("Equal to (==):", x == y)      # False
print("Not equal (!=):", x != y)     # True
print("Greater than (>):", x > y)    # False
print("Less than (<):", x < y)       # True
print("Greater or equal (>=):", x >= y) # False
print("Less or equal (<=):", x <= y)    # True

# Assignment Operators (=, +=, -=, *=, /=, %=, **=)
z = 7    # Assign
z += 3   # z = z + 3 -> z = 10
print("After += 3:", z)
z -= 2   # z = z - 2 -> z = 8
print("After -= 2:", z)
z *= 2   # z = z * 2 -> z = 16
print("After *= 2:", z)
z /= 4   # z = z / 4 -> z = 4.0
print("After /= 4:", z)
z %= 3   # z = z % 3 -> z = 1.0
print("After %= 3:", z)
z **= 3  # z = z ** 3 -> z = 1.0
print("After **= 3:", z)

# Logical Operators (not, and, or)
flag1 = True
flag2 = False

print("Logical NOT (not flag1):", not flag1)  # False
print("Logical AND (flag1 and flag2):", flag1 and flag2)  # False
print("Logical OR (flag1 or flag2):", flag1 or flag2)     # True
