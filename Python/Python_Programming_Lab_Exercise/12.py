# Write a program to demonstrate list slicing and list manipulation.

li = [1, 2, 3, 4, 5]

# slicing
print("First 3:", li[:3])
print("Last 3:", li[-3:])
print("Reverse:", li[::-1])

# manipulation
li.append(7)
li.remove(2)
li.insert(1, 10)

print("Modified list:", li)