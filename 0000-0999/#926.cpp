#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
 
int main() {
    double a,b,c,d,f;
    double S1,S2,SO;
    double P1,P2,p1,p2;
    double G1,G2;
    cin>>a>>b>>c>>d>>f;
    P1= a+b+f;
    p1= P1/2;
    P2= d+c+f;
    p2= P2/2;
    G1=p1*(p1-a)*(p1-b)*(p1-f);
    S1=sqrt(G1);
    G2=p2*(p2-d)*(p2-c)*(p2-f);
    S2=sqrt(G2);
    SO=S1+S2;
    cout<<fixed<<setprecision(4)<<SO;
    return 0;
}
