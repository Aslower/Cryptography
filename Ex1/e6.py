#6.求x[i]与x[j]的最大公因子

import math

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

#import gmpy2
# def batch_gcd(x,y):
#     r = (x*y) % (x*x)
#     return batch_gcd(r/x,x)

seq = []
n=int(input("Input n:"))
for i in range(1,n+1):
    x = int(input("x[%d]="%i))
    seq.append(x)

ans = []
for i in range(0,len(seq)):
    for j in range(i+1,len(seq)):
        ans.append(gcd(seq[i],seq[j]))

print ("Answer:%s"%ans)




#Batch gcd
# def producttree(X):
#        result = [X]
#        while len(X) > 1:
#          X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)]
#          result.append(X)
#        return result
       
# def batchgcd_faster(X):
#        prods = producttree(X)
#        R = prods.pop()
#        while prods:
#          X = prods.pop()
#          R = [R[floor(i/2)] % X[i]**2 for i in range(len(X))]
#        return [gcd(r/n,n) for r,n in zip(R,X)]

