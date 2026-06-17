# Write a program to write and append data to a file.

# Write
file = open("used_files\q18_test.txt", "w")
file.write("Hello World\n")
file.close()

# Append
file = open("used_files\q18_test.txt", "a")
file.write("Appended line\n")
file.close()