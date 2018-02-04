#include <iostream>
#include <cmath>
using namespace std;
 
int sym_level(int number){
    int lo, hi, cnt;
    
    for ( lo = 0, hi = (int)log10((double)number), cnt = 0; lo <= hi; ++lo, --hi )
        if ( ( (number / (int)pow(10.0, lo)) % 10 ) == ( (number / (int)pow(10.0, hi)) % 10 ) )
            ++cnt;
            
    return cnt;
}
 
int main(){
    int num;
    
    cin >> num && num > 0 ;
    cout << sym_level(num) <<endl;
    
    return 0;
}
