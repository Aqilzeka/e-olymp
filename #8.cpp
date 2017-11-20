#include <iostream>
#include <cmath>
using namespace std;

int squares(int  n)
{
    int s = static_cast<int>(floor(sqrt(static_cast<double>(n))));
    int k = n - s * s;
    int p = (k == 0) ? 0 : (k - 1)/s + 1;
    return 2*s*(s+1) + p*3 + (k-p)*2;
}

int main()
{
        int  squares_count;
        cin >> squares_count; 
		       
        cout<< squares(squares_count);    
}
