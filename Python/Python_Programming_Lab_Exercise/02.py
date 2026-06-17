# Write a program to perform all arithmetic operations on user input numbers.

# input 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b == 0:
    print("Division, Floor Division, Modulus not possible")
else:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)

print("Power:", a ** b)