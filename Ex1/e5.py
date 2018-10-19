# x^a=b(mod N)求x，开任意次方


def exp(a,b,N):
	r=a%(N-1)
	res=pow(b%N,1/r)
	return res


a=int(input("a="))
b=int(input("b="))
N=int(input("N="))
print(exp(a,b,N))