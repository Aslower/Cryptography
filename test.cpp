#include <stdio.h>
#include <iostream>
using namespace std;

void func(int *p)
{
    static int num = 4;
    p = &num;
    (*p)--;
}
int main()
{
    int i = 5;
    int *p;
    p=&i;

    cout<<&p<<endl;
    cout<<&i<<endl;
    cout<<p<<endl;
    cout<<*p<<endl;

    func(&i);
    printf("%d", *p);
    return 0;
}
/*
void func(int **p)
{
    static int num = 4;
    *p = &num;
    (**p)--;
}
int main()
{
    int i = 5;
    int *p = &i;
    func(&p);
    printf("%d",*p);
    return 0;
}
*/