# Write a program to count how many times a given element appears in a list.

list = [1,2,3,4,5,6,7,8,9,10,1,2,3,5,1,7,2,1,8,9,0]
key = int(input("Enter number = "))
count=0
for i in list:
    if i==key:
        count+=1
print(f"{key} appears {count} times")