# Write a program to find the largest and smallest element in a list.
list=[1,2,3,4,5,6,7,8,9,10]
min=list[0]
max=list[0]
for i in list:
    if min>i:
        min=i
    if max<i:
        max=i
print(f"Smallest number = {min}\nLargest number = {max}")