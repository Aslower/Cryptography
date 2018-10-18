#给定同余式 ax = b (mod N)，即给定整数a、b和N，求x

def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)

#1 即求a的乘法逆元
# def Congruence(a,b,N):   
#     if gcd(a,N)==1 and b%a==0:
#         print("The answer(s) as follow:")
#         x=0
#         for x in range(0,N+1):
#             if (b-a*x)%N==0:
#                 print("x(mod n)=%d"%x)
#     else:
#         print("No Answer!")

#2 用gcd(a,N)==1，x=a/b(mod N)——> (x-b/a)(mod N)=0 即 x=b/a(mod N)求得！
#其中要解决a/b的问题


#3 用egcd解， 要满足gcd(a,N) | b 才有解
def Congruence_egcd(a,b,d,x,y):
        if b==0:
            x,y,d=1,0,a
        else:
            Congruence_egcd(b,a%b,d,x,y)
            temp=x;x=y;y=temp-(a/b)*y

            
#4 
def Congruence(a,b,N): 
    r=b%N
    for x in range(0,N+1):
        if((a*x-r)%N==0):
            print("x(mod n)=%d"%x)

    
a,b,N=int(input("a=")),int(input("b=")),int(input("N="))
Congruence(a,b,N)

x,y=0,0
d=gcd(a,N)%b
Congruence_egcd(a,b,d,x,y)
if b%d!=0:
    print("No solution!")
else:
    x=x*(b/d)%b



