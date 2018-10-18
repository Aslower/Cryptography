#include<iostream>
using namespace std;

int main()
{
	long long a;
	long long k;
	long long c;
	long long b;
	
	
	cout << "请输入一个十进制的数" << endl;
    while(1){
        k = 1;
	c = 0;
	cin >> a;
	if (a >= 0)
	{
		for (k = 1; a != 0; k = k * 10)
		{
			b = a % 2;
			a = a / 2;
			
			c = c + b * k;
		}

		cout << "该数字的二进制为" << "0" <<c<<endl;
	}
	if (a < 0)
	{
		a = -a;
		for (k = 1; a != 0; k = k * 10)//化二进制
		{
			b = a % 2;
			a = a / 2;
			c = c + b * k;
		}
		cout << "该数字的二进制为"<<"1" <<c<<endl;

	}
    }
	return  0;

}
