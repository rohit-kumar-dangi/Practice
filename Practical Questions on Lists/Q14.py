# Write a program to find the frequency of each element in a list.

list = [1,2,3,4,5,6,7,8,9,10,1,2,3,5,1,7,2,1,8,9,0]
u_list = set(list)
dict_list={}
for i in u_list:
    count=0
    for j in list:
        if i==j:
            count+=1
    dict_list[str(i)]=str(count)

for i in dict_list:
    print(i," : ",dict_list[i])