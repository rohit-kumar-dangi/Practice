# Write a program to check whether a given element exists in a tuple.

Tuple=(1,2,3,4,5,6,7,8,9,10)
key=int(input("Enter key : "))
flag=False
for i in Tuple:
    if i==key:
        flag=True
        break
if flag:
    print("Given key is found")
else:
    print("Given key is not found")