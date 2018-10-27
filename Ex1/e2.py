#Vertify the Egcd

def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)

def egcd(a,b):
    r0,r1,s0,s1=1,0,0,1
    while b:
        q,a,b=int(a/b),b,a%b
        r0,r1=r1,r0-q*r1
        s0,s1=s1,s0-q*s1
    return a,r0,s0

# a2,b2=int(input("a=")),int(input("b="))
# a=gcd(a2,b2)
# aa,r,s=egcd(a2,b2)

# print(r,s,aa)
# if aa==a and (r*a2+s*b2)==a:
#     print("Egcd is right")
# else:
#     print("Egcd is wrong")
