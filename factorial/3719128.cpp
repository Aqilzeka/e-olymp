#include <iostream>
using namespace std;

long double fact(int N)
{
    int total = 1;
    while(N>0){
        total *= N;
        N-=1;
    }
    return total;
}

int main()
{
    int N;
    cin >> N;
    cout << fact(N) << endl;
    return 0;
}