# Write a program to separate positive and negative numbers from a list.

list = [-1,-2,3,4,5,6,-7,8,9]
positive_list=[]
negative_list=[]
for i in list:
    if i<0:
        negative_list.append(i)
    else:
        positive_list.append(i)
print(f"Positive list = {positive_list}\nNegative list = {negative_list}")