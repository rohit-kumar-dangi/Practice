# Write a program to count even and odd numbers in a given list

list=[1,2,3,4,5,6,7,8,9,10]
c_odd=0
c_even=0
for i in list:
    if i%2==0:
        c_even+=1
    else:
        c_odd+=1
print(f"Number of odd number in list = {c_odd}\nNumber of even number in list = {c_even}")