# Write a program using for loop to print multiplication table of a number

num = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{num} * {i} = {i * num}")