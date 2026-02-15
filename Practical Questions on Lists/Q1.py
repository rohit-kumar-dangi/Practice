# Write a program to input n elements into a list and display them using a loop.
list =[]
for i in range(int(input("Enter limit : "))):
    list.append(int(input(f"Enter {i+1} number : ")))

for i in list:
    print(i)