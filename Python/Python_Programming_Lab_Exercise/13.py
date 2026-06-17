# Write a program to perform tuple operations and demonstrate immutability.

t = (1, 2, 3, 4, 5)

print("Element : ", t[1])

print("Count of 2 : ", t.count(2))
print("Index of 3 : ", t.index(3))

# immutability
# t[0] = 10    Error (cannot change tuple)
print("Tuple : ", t)