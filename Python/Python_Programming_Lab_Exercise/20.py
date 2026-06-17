# Write a program to demonstrate file pointer operations using seek().

file = open("used_files\q20_test.txt", "r")

print(file.read(2))   # read first 2 chars

file.seek(0)          # move pointer to beginning

print(file.read(5))   # read again first 5 charcter

file.close()