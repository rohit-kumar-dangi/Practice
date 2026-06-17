# Write a program to count frequency of characters in a string.

s = input("Enter string: ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key,value in freq.items():
    print(f"{key} : {value}")