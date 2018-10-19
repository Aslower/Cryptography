#GCD with recursion

def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)

def iteration_gcd(a,b):
    while 1:
        if a<b:
            a,b=b,a
        if b==0:
            return a
        else:
            a,b=b,a%b


a=int(input("a="))
b=int(input("b="))

print("gcd(a,b)=%d"%gcd(a,b))
print("iteration_gcd(a,b)=%d"%iteration_gcd(a,b))