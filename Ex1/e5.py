import math

def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)

# a,b,n=int(input()),int(input()),int(input())
# count=0

# for x in range(1,n+1):
#     if gcd(x,n)==1:
#         count=count+1
    
# def Euler():
#     c=a%count
#     xx=pow(b,float(1)/float(c))
#     print(xx)

# Euler()

#test teamview

import sys
import math
#import gmpy2

def phi(x):
    res, a = x, x
    for i in range(2,int(math.sqrt(a)+1)):
        if(a%i==0):
            res = res/i*(i-1)
            while(a%i==0):
            	a/=i
    if(a>1):
    	res = res/a*(a-1)
    return res


def egcd(a,b):
	if(b==0):
		x,y,d=1,0,a
		return x,y,d
	else:
		x,y,d=egcd(b,a%b)
		tmp=x
		x=y
		y=tmp-(a/b)*y
		return x,y,d

a = int(input("input a: "))
b = int(input("input b: "))
N = int(input("input N: "))
r = int (phi(N))
x,y,d = egcd(a,r)
if(d==1):
	def egcd1(a, b):
		r0, r1, s0, s1 = 1, 0, 0, 1
		while (b):
			q, a, b = a // b, b, a % b
			r0, r1 = r1, r0 - q * r1
		return r0, r1
	if (gcd(a, r) == 1):
		x, y = egcd1(a, r)
		e = x % r
	print (pow(b,e,N))
else:
	print("No solution")
