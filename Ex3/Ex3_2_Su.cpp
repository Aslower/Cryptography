#include <iostream>
#include <stdio.h>
using namespace std;

 //a+b
int poly_add(int a, int b) {
 
    return a ^ b;
}

//a*b
int poly_mul(int a, int b) {
    int result;
    if(b & 0x01) {
        result = a;
    }else {
        result = 0;
    }
    for(int temp = 0x02;temp <= 0x80;temp = temp << 1) {
        if (b & temp) {
            a = a << 1;
            if(a & 0x100) {
                a = a ^ 0x1B;
            }
            a = a & 0xFF;
            result = result ^ a;
        }else {
            a = a << 1;
            if(a & 0x100) {
                a = a ^ 0x1B;
            }
        }
    }
    return result & 0xFF;
}

//除法 a/b = q....r
 
// 1.判断两个数的位数 求差，如果b>a的话回q = 0；r = b；
// 2.将b左移位数差
// 3.a和b左异或运算 
int numberOfDigits(int a) {
    int count = 0;
    while(a) {
        count++;
        a = a >> 1;
    }
    return count;
}
 
void poy_dvid(int a,int b,int &q ,int &r) {
    // int digit_a = numberOfDigits(a);
    int digit_a = numberOfDigits(a);
    int digit_b = numberOfDigits(b);
    b = b << (digit_a - digit_b);
    int temp = 0x01 << (digit_a - 1);
    for(int i = 0;i <= digit_a - digit_b;i++) {
        if(a & temp) {
            a = a ^ b;
            b = b    >> 1;
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
 
 
 
// 模a下求b的逆
int poy_inv(int a, int b) {
    int r_0,s_0;
    int r_1,s_1;
    r_0 = 1;s_0 = 0;
    r_1 = 0;s_1 = 1;
    int temp_a = a;
    while(b) {
        int q = 0,r = 0;
        poy_dvid(a,b,q,r);
        a = b;b = r;
        int temp_r_0 = r_0;
        int temp_s_0 = s_0;
        r_0 = r_1;s_0 = s_1;
        r_1 = temp_r_0 ^ poly_mul(q,r_1);
        s_1 = temp_s_0 ^ poly_mul(q,s_1);
    }
    if(s_0 < 0)
        s_0 = s_0 ^ temp_a;
    return s_0;
}

 
 
int poly_logarithm(int g,int x) {
    int y = 1;
    int result = g;
    while(result != x) {
        y = poly_mul(y,g);
        result = poly_mul(g,y);
    }
    return y;
}
 
 
 
// 1.建一个数组
// 2.按位求异或的算法
int byte_xor(int a) {
    int temp = 0x01;
    int result = 0;
    while(a) {
        result = result ^ (a & temp);
        a = a >> 1;
    }
    return result;
}
 
 
 
int main()
{
    int mat[8] = {0xF8, 0x7C, 0x3E,0x1F,0x8F,0xC7,0xE3,0xF1};
    int c = 0x63;
    int a = 0x11B;
    int s[16][16];
    for(int i = 0;i < 16;i++) {
        for(int j = 0;j < 16;j++) {
            s[i][j] = i * 16 + j;
            printf("%x",s[i][j]);
            s[i][j] = poy_inv(a,s[i][j]);
            printf("/%x ",s[i][j]);
            int result = 0;
            int temp = 0x80;
            for(int k = 0;k < 8;k++) {
                int temp_result = byte_xor(s[i][j] & mat[k]) ^ byte_xor(temp & c);
                result = (result << 1) + temp_result;
                temp = temp >> 1;
            }
            s[i][j] = result;
        }
        printf("\n");
    }
 
    printf("\n\n\n\n\n");
    for(int i = 0;i < 16;i++) {
        for(int j = 0;j < 16;j++)
            printf("%02x ", s[i][j]);
        printf("\n");
    }
 
    return 0;
}