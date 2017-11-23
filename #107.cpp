#include<iostream>
using namespace std;
 
int main ()
{
    int N, p;
    cin >> N;
    if (N % 100 > 65)
        p += (N / 100 + 1) * 100;
    else
    {
        int a = N % 100;
        p += (N/100) * 100;
        if (a % 20 > 15)
            p += (a / 20 + 1) * 30;
        else
        {
            int b = (a % 20);
            p += (a / 20) * 30;
            p += b*2;
        }
    }
    cout << p;
    return 0;
}
