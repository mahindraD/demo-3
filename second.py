# fint a given number is prime or not

def prime(n):
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

n=int(input("enter number"))
print("prime =",prime(n))