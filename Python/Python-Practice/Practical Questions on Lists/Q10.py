# Write a program to find the second largest element in a list.

list=[1,3,4,2,5,6,7,9,8,10]
fl=list[0]
sl=list[0]
for i in list:
    if fl<i:
        sl=fl
        fl=i

print(fl,sl)
