# Write a program to find common elements between two lists.

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[2,3,4,11,44,23,11,34]

def com_ele(list1,list2):
    com_list=[]
    for i in list1:
        for j in list2:
            if i==j:
                com_list.append(i)
    print(com_list)

com_ele(list1,list2)