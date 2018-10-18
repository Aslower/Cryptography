#给定同余式 ax = 1 (mod N)，即给定整数a和N，求x（逆元）
#除以一个数取模 = 乘以这个数的逆元取模
# a * x ≡ 1 ( mod  m )   =>    a * x = 1 + m * k     
# a * x = 1 + m * k      =>    a * x – m * k = 1   (gcd（a，m）=1)


def egcd(a, b):
    x, y, d = egcd(b, a % b) # q = gcd(a, b) = gcd(b, a%b)
    x, y = y, (x - (a // b) * y)
    return x, y, d

# def egcd(a,b):
#     r0,r1,s0,s1=1,0,0,1
#     while b:
#         q,a,b=a/b,b,a%b
#         r0,r1=r1,r0-q*r1
#         s0,s1=s1,s0-q*s1
#     return d,r0,s0

def Invert():
   a,N=int(input("a=")),int(input("b="))
   x,k,d=egcd(a,N)
   if x==int & x>0:
       print("逆元存在为：%d"%x)
   else:
       print("逆元不存在")

Invert()


