def cal(num):
    sum=0
    fact=1
    for i in range(1,num+1):
        fact*=i
        if i%2==0:
            sum-=i**i/fact
        else:
            sum+=i**i/fact
    return sum

num=int(input("Enter number : "))
print(cal(num))