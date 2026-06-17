# Demonstrate use of break, continue, and pass in loops.

# break
for i in range(5):
    if i == 3:
        print("Break at:", i)
        break
    print("i =", i)

# continue
for i in range(5):
    if i == 3:
        continue
    print("i =", i)

# pass
for i in range(5):
    if i == 3:
        pass
    print("i =", i)