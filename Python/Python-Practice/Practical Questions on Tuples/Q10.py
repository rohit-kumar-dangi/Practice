# Write a program to create a new tuple containing only positive numbers.

def pos_tuple():
    n=int(input("Enter limit : "))
    tup()
    for i in range(1,n+1):
        if i%2==0:
            tup=tup+2
    return tup

print(pos_tuple)