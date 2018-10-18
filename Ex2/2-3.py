import random

def Group(p,q):
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
    print(Group(p_prime[i],q_prime[i]))

