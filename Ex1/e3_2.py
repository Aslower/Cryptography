import e4


a=int(input("a="))
b=int(input("b="))

N=int(input("N="))

aa=e4.Inv(a,N)
print(b*aa%N)