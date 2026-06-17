# Write a program to copy contents of one file to another.

f1 = open("used_files\q19_test.txt", "r")
data = f1.read()
f1.close()

f2 = open("used_files\q19_copy.txt", "w")
f2.write(data)
f2.close()