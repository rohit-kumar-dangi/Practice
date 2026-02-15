# Write a program to merge two lists and display the result.

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,3,4,2,5,6,7,9,8,10]

def merge_list(list1,list2):
    for i in list2:
        list1.append(i)
    return list1
merged_list=merge_list(list1,list2)
print(merged_list)