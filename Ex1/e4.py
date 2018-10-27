#给定同余式 ax = 1 (mod N)，即给定整数a和N，求x（逆元）


#除以一个数取模 = 乘以这个数的逆元取模
# a * x ≡ 1 ( mod  m )   =>    a * x = 1 + m * k     
# a * x = 1 + m * k      =>    a * x – m * k = 1   (gcd（a，m）=1)


def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)

def egcd(a,b):
    r0,r1,s0,s1=1,0,0,1
    while b:
        q,a,b=a//b,b,a%b
        r0,r1=r1,r0-q*r1
        s0,s1=s1,s0-q*s1
    return r0,s0,a
    #return r0



def Inv(a,N):
    r,s,d=egcd(a,N)
    if d==1:
        return r%N
    else:
        return 0


if __name__ == "__main__":
    a=int(input("a="))
    N=int(input("N="))
    print(Inv(a,N))


    
