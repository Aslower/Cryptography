K.<a> = FiniteField(256)
# 先定义曲线的A和B参数！！！！A = a^3 = 8, B = a^2+a+1 = 7
E = EllipticCurve( K, [1,(a^3),0,0,(a^2+a+1)])
# print E.points()
print E.cardinality()

# point arithmetic
P = E(a + 1 , a^6 + a^4 + a + 1 )
Q = E(a^3 , a^7 + a^5 + 1 )
print P+Q
print P.order()

#generator
print E.gens()
