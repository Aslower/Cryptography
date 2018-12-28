# import sagemath

# K.<a> = FiniteField(256)
# # 先定义曲线的A和B参数！！！！A = a^3 = 8, B = a^2+a+1 = 7
# E = EllipticCurve( K, [1,(a^3),0,0,(a^2+a+1)])
# # print E.points()
# print E.cardinality()

# # point arithmetic
# P = E(a + 1 , a^6 + a^4 + a + 1 )
# Q = E(a^3 , a^7 + a^5 + 1 )
# print P+Q
# print P.order()

# #generator
# print E.gens()


#编程实现以下椭圆曲线相关功能。考虑在GF(2^8)上的E(GF(2^8))，参考CANS的310-312页。
#1、统计该椭圆曲线上点的个数，即点群的Order。
#2、现实E上的点加法；即实现求：P+P、P+Q和nP的程序。
#3、这个曲线上的点群是循环群吗？如果是，求一个生成元。
#4、编程画出曲线上所有的点。


import matplotlib.pyplot as plt

table = {}
arc_table = {}

table[0] = 1
arc_table[1] = 0

for i in range(1, 255):
    table[i] = (table[i-1] << 1) ^ table[i-1]
    if(table[i] & 0x100): table[i] ^= 0x11b

    arc_table[ table[i] ] = i
#乘法
def multiplication(x ,y):
    if((not x) or (not y)): return 0
    return table[ (arc_table[x] + arc_table[y]) % 255 ]
#除法
def division(x, y):
    inverse = table[ (255 - arc_table[y]) % 255 ]
    return multiplication(x, inverse)



class ECC(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.discriminant = multiplication(4,multiplication(a,multiplication(a,a))) ^ multiplication(27,multiplication(b,b))
        #a、b要满足：4a^3+27b^2!=0，则可基于E(a,b)定义一个群
        if not self.isSmooth():
            raise Exception("The curve is not smooth!")
        
    def isSmooth(self):
        return self.discriminant != 0

    def testPoint(self, x, y):
        return multiplication(y, y) ^ multiplication(x, y) == multiplication(x, multiplication(x, x)) ^ multiplication(self.a, multiplication(x, x)) ^ self.b
        #GF(2^m)上的椭圆曲线：y^2+xy=x^3+ax^2+b
    def __str__(self):
        return 'y^2 + x*y = x^3 + %G*x^2 + %G' % (self.a, self.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

class Point(object):

    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x % 256
        self.y = y % 256
        if not curve.testPoint(x, y):#x、y是否满足y^2+xy=x^3+ax^2+b
            raise Exception("The point is not on the elliptic curve." )

    def __neg__(self):
        return Point(self.curve, self.x, self.x ^ self.y)

    def __add__(self, Q):
        if isinstance(Q, Setstart):
            return self

        x1, y1, x2, y2 = self.x, self.y, Q.x, Q.y

        if self == -Q: return Setstart(self.curve)

        #P+P
        if(x1, y1) == (x2, y2):
            r =  x1 ^ division(y1, x1)

            x3 = multiplication(r, r) ^ r ^ self.curve.a
            y3 = multiplication(x1, x1) ^ multiplication((r ^ 1), x3)

        #P=(x1,y1),Q=(x2,y2)，P!=Q    
        else:
            r = division((y2 ^ y1), (x2 ^ x1))

            x3 = multiplication(r, r) ^ r ^ x1 ^ x2 ^ self.curve.a
            y3 = multiplication(r, x1 ^ x3) ^ x3 ^ y1
            
        return Point(self.curve, x3, y3)
    
    #np
    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("Error:Not an integer!")
        else:
            if n < 0:
                return -self * -n
            if n == 0:
                return Setstart(self.curve)
            else:
                Q = self
                R = self if n & 1 == 1 else Setstart(self.curve)#n为奇数，R=P(self)，否则R=0

                i = 2
                while i <= n:
                    Q = Q + Q  #2Q、4Q、8Q......
                    
                    if n & i == i:   #n为奇数，R=2^n+R，n为偶数，R=2^n+0
                        R = Q + R

                    i = i << 1  
        return R

    def __rmul__(self, n):
        return self * n

    def __eq__(self, other):
        return (self.x, self.y, self.curve) == (other.x, other.y, other.curve)

    def __str__(self):
        return '(%G, %G)' % (self.x, self.y)


class Setstart(Point):

    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Setstart"

    def __neg__(self):
        return self

    def __add__(self, Q):
        return Q

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("Error:Not an integer!")

        else:
            return self

X = []
Y = []

curve = ECC(2, 4)
zero = Setstart(curve)
num = 0
for x in range(256):
    for y in range(256):
        if curve.testPoint(x,y):  #是否为椭圆曲线上的点
            num += 1
            X.append(x)
            Y.append(y)
order=num+1     #满足y^2+xy=x^3+ax^2+b的所有的点和元素O（无穷远点）所组成的点集：E(a,b)
print("点群的阶为：" + str(order))  


print("生成元：")
gen_num = 0
for x,y in zip(X,Y):
    tmp = Point(curve, x, y)
    Num = Point(curve, x, y)
    myOrder = 1
    while(True):
        tmp = tmp + Num #椭圆曲线上的点进行加运算
        myOrder += 1
        if isinstance(tmp, Setstart):break
    if myOrder == order: 
        print(Num)
        gen_num += 1
        

print("生成元个数：" + str(gen_num))

#画出曲线上所有的点
plt.title("GF(256)elliptic curve ") 
plt.xlim(xmax=256,xmin=0)
plt.ylim(ymax=256,ymin=0)
plt.plot(X, Y, 'ro')
plt.show()