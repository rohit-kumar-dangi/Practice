# Write a program to count occurrences of each element in a tuple.

Tuple=(1,2,3,1,4,5,1,6,7,8,9,2,10)
u_tuple = set(Tuple)
dict_tuple={}
for i in u_tuple:
    count=0
    for j in Tuple:
        if i==j:
            count+=1
    dict_tuple[str(i)]=str(count)

for i in dict_tuple:
    print(i," : ",dict_tuple[i])
