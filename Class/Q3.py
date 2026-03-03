def fun(*args):
    a=args
    sum=0
    for i in a:
        sum+=i
    return sum
    
a=fun(1,2,3,4,5,6,7,8,9)
print(type(a))
print(a)