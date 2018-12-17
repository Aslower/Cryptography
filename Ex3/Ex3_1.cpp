#include <iostream>
#include <cstdio>
#include <stdio.h>
using namespace std;

// int gcd(int a,int b){
//     if(b==0)    
//         return a;
//     else     
//         return gcd(b,a % b);
// }

int gcd(int a, int b){
	if(a < b){
		a ^= b;
		b ^= a;
		a ^= b;}

	while(b != 0){
		int temp = a;
		a = b;
		b = temp % b;}

	return a;
}

//a+b  
//直接异或运算（除法也是异或）
int GF_add(int a, int b){ 
    return a ^ b;
    }

//a*b  
//域中元素对应的多项式的乘法运算，相加时为模2加法
//在乘积得出来的多项式次数大于7时，我们需要对多项式在GF(2)上关于P(x)）求余数
int GF_mul(int a, int b){
    int res;
    
    if(b & 0x01)
        res=a;
    else
        res=0;
    for(int temp = 0x02;temp <= 0x80;temp = temp << 1) {
        if (b & temp) {
            a = a << 1;
            if(a & 0x100) {
                //最高位是1的话，左移一位的同时要异或0x1B
                a = (a<<1) ^ 0x1B;
            }
            a = a & 0xFF;
            res= res ^ a;
        }else {
            a = a << 1;
            if(a & 0x100) {
                a = (a<<1) ^ 0x1B;
            }
        }
    }//若溢出则，需要用到P(x)相加(异或)来消去
    return res;
}

// numbers of binary-bit to represent a decimal
int numberOfDigits(int a) {
    int temp = 0x80;
    int count = 8;
    while(!(a & temp)) {
        count--;
        temp = temp >> 1;
    }
    return count;
}

//a/b
void GF_dvid(int a,int b,int &q ,int &r ) {
    // int digit_a = numberOfDigits(a);
    int digit_a = 9;
    int digit_b = numberOfDigits(b);
    printf("digit_a = %d,digit_b = %d\n",digit_a,digit_b);
    b = b << (digit_a - digit_b);
    printf("b = %X\n", b);
 
    int temp = 0x01 << (digit_a - 1);
    printf("temp = %d\n",temp);
 
    for(int i = 0;i <= digit_a - digit_b;i++) {
        if(a & temp) {
            a = a ^ b;
            b = b >> 1;
            q = (q << 1) + 1;
            temp = temp >> 1;
        }else {
            b = b >> 1;
            q = q << 1;
            temp = temp >> 1;
        }
    }
    r = a;
}

//乘法逆元 Euclid
int GF_inv(int a, int b) {
    int r_0,s_0;
    int r_1,s_1;
    r_0 = 1;s_0 = 0;
    r_1 = 0;s_1 = 1;
    int temp_a = a;
    while(b) {
        int q = 0,r = 0;
        GF_dvid(a,b,q,r);
        a = b;b = r;
        int temp_r_0 = r_0;
        int temp_s_0 = s_0;
        r_0 = r_1;s_0 = s_1;
        r_1 = temp_r_0 ^ GF_mul(q,r_1);
        s_1 = temp_s_0 ^ GF_mul(q,s_1);
    }
    if(s_0 < 0)
        s_0 = s_0 ^ temp_a;
    return s_0;
}

//Logarithm
int GF_logarithm(int g,int x) {
    int y = 1;
    int result = g;
    while(result != x) {
        y = GF_mul(y,g);
        result = GF_mul(g,y);
    }
    return y;
}




int main(int argc, char const *argv[])
{
    //不可约多项式 P(x) = x8 + x4 +x3 + x2 + 1
    //==> x8=x4+x3+x2+1   [1 0001 1101]
    cout<<GF_mul(129,5)<<endl;
   for(int i=1;i<20;i++)
    cout<<numberOfDigits(i);


    return 0;
}
