# Write a program to check whether a list is sorted or not.

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,3,4,2,5,6,7,9,8,10]

def check_sort(list):
    is_sort=True
    for i in range(len(list)-1):
        if list[i]<list[i+1]:
            continue
        is_sort=False
    if is_sort:
        print("Given list is sorted")
    else:
        print("Given list is not sorted")

check_sort(list1)
check_sort(list2)