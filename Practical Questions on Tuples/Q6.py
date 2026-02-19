# Write a program to find the maximum and minimum element in a tuple.

Tuple=(1,2,3,4,5,6,7,8,9,10)
min=Tuple[0]
max=Tuple[0]
for i in Tuple:
    if i<min:
        min=i
    if i>max:
        max=i
print("Max = ",max)
print("Min = ",min)