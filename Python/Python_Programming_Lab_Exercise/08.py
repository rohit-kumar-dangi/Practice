# Write a program using while loop to compute sum of first N natural numbers.

num = int(input("Enter a number : "))
i=1
sum=0
while(i<=num):
    sum+=i
    i+=1
print(f"Sum of {num} Natural nnumber = {sum}")