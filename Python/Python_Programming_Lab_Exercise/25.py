# Write a program demonstrating multiple exceptions handling.

try:
    lst = [1, 2, 3]
    print(lst[5])      # IndexError
    x = int("abc")     # ValueError

except IndexError:
    print("Index out of range")

except ValueError:
    print("Invalid conversion")

except Exception as e:
    print("Other error:", e)