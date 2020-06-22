from math import sqrt
def primefact(n):
    l=[]
    while n%2==0:
        l.append(2)
        n=n/2
    for i in range(3,int(sqrt(n))+1,2):  
        while n%i==0:
            l.append(i)
            n=n/i  
    if n>2:
        l.append(n)
    return l
a=primefact(int(input()))
print(a[int(input())-1])
