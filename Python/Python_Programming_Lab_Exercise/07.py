# Write a program to iterate through string, list, and dictionary using loops.

print("String")
str = "Rohit"
for s in str:
    print(s, end=" ")

print("List")
li = [1,2,3,4,5]
for i in li:
    print(i, end=" ")

print("Dictionary")
dic = {"Name" : "Rohit",
       "Roll" : 42,
       "Course" : "BCA"}
for key, value in dic.items():
    print(f"{key} : {value}", end=" ")