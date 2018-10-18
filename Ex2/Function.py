import math
import random

def gcd(a,b):
    if b==0:    
        return a
    else:       
        return gcd(b,a % b)


def Q1():
    n=int(input("Enter n of Multiplicative group of integers modulo p:"))
    print("Order is %d"%(n-1))

    #Euler's Theorem
    generator=[]
    count_gen=0
    for i in range(2,n-1):
        if gcd(i,n)==1:
            generator.append(i)
            count_gen+=1
    print("All generators:%s "%generator)
    print("The number of generators is %d"%count_gen)
    ##Conjecture


def Q2():
    n=int(input("Enter n of Multiplicative group of integers modulo n:"))
    Zn=[]
    cout=0
    for i in range(1,n):
        if gcd(i,n)==1:
            Zn.append(i)
            cout+=1
    print(Zn)
    print(cout)


def Q3_Group(p,q):
    g = (random.randint(2, p-1) ** ((p-1)//q))%p
    # g=random.randint(0,p-1)**q
    while g==1:
        g = (random.randint(2, p-1) ** ((p-1)//q))%p
    G =[]
    for i in range(1,p):
        if g**i%p == 1:
            G.append(1)
            break
        G.append((g ** i) % p)
    return g, len(G), G



prime=[2,3,5]
for i in range(7,101):
    prime.append(i)
    for j in range(2,i):
        if i%j==0:
            prime.remove(i)
            break       
print("primes:%s"%prime)    
#Get the primes
q_prime=[];p_prime=[]
for q in prime:
    p=2*q+1
    if p in prime:
        p_prime.append(p)
        q_prime.append(q)

print("p:%s"%p_prime)
print("q:%s"%q_prime)
print("\n")

for i in range(0,len(p_prime)):
    print(Q3_Group(p_prime[i],q_prime[i]))


