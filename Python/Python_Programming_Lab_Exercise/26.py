# Write a program using finally and custom exceptions.

class NegativeNumberError(Exception):
    pass

try:
    n = int(input("Enter number: "))
    
    if n < 0:
        raise NegativeNumberError("Negative not allowed")
    
    print("Number:", n)

except NegativeNumberError as e:
    print(e)

finally:
    print("Execution completed")