# Write functions to organize a program that performs basic operations on strings and lists.

def string_operations(s):
    print("Upper:", s.upper())
    print("Reverse:", s[::-1])
    print("Length:", len(s))

def list_operations(lst):
    print("Sum:", sum(lst))
    print("Max:", max(lst))
    print("Sorted:", sorted(lst))

# Main
s = "ROhit"
lst = [1,2,3,4,5]

string_operations(s)
list_operations(lst)