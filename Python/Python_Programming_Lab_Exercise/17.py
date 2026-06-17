# Write a program to read contents of a file using read(), readline(), and readlines().

file = open("used_files\q17_test.txt", "r")

print("Using read():")
print(file.read())

file.seek(0)

print("Using readline():")
print(file.readline())

file.seek(0)

print("Using readlines():")
print(file.readlines())

file.close()