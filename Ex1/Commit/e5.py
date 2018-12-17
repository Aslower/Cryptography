# x^a=b(mod N)求x，开任意次方
import e4

def exp(a,b,N):
	r=a%(N-1)
	res=pow(b%N,1/r)
	return res

def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)

# a=int(input("a="))
# b=int(input("b="))
# N=int(input("N="))
# print(exp(a,b,N))


#RSA
def Phi(N):
	count=1
	for i in range(2,N):
		if gcd(i,N)==1:
			count+=1
	return count

def Rsa(a,b,N):
	phi=Phi(N)
	d=e4.Inv(a,phi)
	# print(phi)
	# print(d)
	if gcd(d,phi)==1:
		return pow(b,d,N)
	else:
		return 0

a=int(input("a="))
b=int(input("b="))
N=int(input("N="))
print(Rsa(a,b,N))#5,2,6