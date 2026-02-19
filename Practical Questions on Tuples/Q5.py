# Write a program to count even and odd numbers in a tuple.

Tuple=(1,2,3,4,5,6,7,8,9,10)
odd_count=0
even_count=0
for i in Tuple:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Total numbers of odd nummber = ",odd_count)
print("Total numbers of even nummber = ",even_count)