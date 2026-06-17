# Write a program to handle exceptions using try-except blocks.

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")