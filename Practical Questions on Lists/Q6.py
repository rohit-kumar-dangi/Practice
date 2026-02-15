# Write a program to reverse a list using a loop (without using built-in functions).

list=[1,2,3,4,5,6,7,8,9,10]
l=int(len(list))
for i in range(int(l/2)):
    temp=list[i]
    list[i]=list[l-i-1]
    list[l-i-1]=temp
print(list)