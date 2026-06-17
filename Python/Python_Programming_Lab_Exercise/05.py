# Write a program using nested if to classify a number (positive, negative, zero).

num = int(input("Enter a number : "))
if num>=0:
    if num>0:
        print("Number is Positive")
    else:
        print("Number is Zero")
else:
    print("Number is Negative")