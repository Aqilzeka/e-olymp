#include <iostream>
using namespace std;
int sqrt(int a)
{
    int s = 0;
    while(a > 0)
    {
        s += a % 10;
        a /= 10;
    }
    if(s > 9) return sqrt(s);
    else return s;
}
int main()
{
    int a;
    
    cin >> a;
    cout << sqrt(a) << endl;

    return 0;
}
